'''
    Created on ?
    @author: Brian Adair
    
'''
import rubik.check as check
import random
import math
from pickle import TRUE, FALSE

class Cube:
    '''
    Rubik's cube
    '''
    valid_operations = 'FfRrBbLlUuDd'
    
    faceCorners = [0,2,8,6]
    faceEdges = [1,3,5,7]
    midIncrement = 4
    topEdgeIncrement = faceEdges[0]
    leftEdgeIncrement = faceEdges[1]
    rightEdgeIncrement = faceEdges[2]
    leftEdgeIncrement = faceEdges[3]
    faceIncrement = 9
    
    maxSideLocation = 35
    
    face_map = {
        'F': [0,1,2,3,4,5,6,7,8],
        'R': [9,10,11,12,13,14,15,16,17],
        'B': [18,19,20,21,22,23,24,25,26],
        'L': [27,28,29,30,31,32,33,34,35],
        'U': [36,37,38,39,40,41,42,43,44],
        'D': [45,46,47,48,49,50,51,52,53]
    }
    
    faceAdjMap = {
        'F': {0: [29,42],
              1: [43],
              2: [9,44],
              3: [32],
              5: [12],
              6: [35,45],
              7: [46],
              8: [15,47]},    
        'R': {9: [2,44],
              10: [41],
              11: [18,38],
              12: [5],
              14: [21],
              15: [8,47],
              16: [50],
              17: [24,53]},   
        'B': {18: [11,38],
              19: [37],
              20: [27,36],
              21: [14],
              23: [30],
              24: [17,53],
              25: [52],
              26: [33,51]},   
        'L': {27: [20,36],
              28: [39],
              29: [0,42],
              30: [23],
              32: [3],
              33: [26,51],
              34: [48],
              35: [6,45]},    
        'U': {36: [20,27],
              37: [19],
              38: [11,18],
              39: [28],
              41: [10],
              42: [0,29],
              43: [1],
              44: [2,9]},    
        'D': {45: [6, 35],
              46: [7],
              47: [8,15],
              48: [34],
              50: [16],
              51: [26,33],
              52: [25],
              53: [17,24]}
    }
    
    rotation_map = {
        'F':{ '1':'3','2':'6','3':'9',
              '4':'2','6':'8',
              '7':'1','8':'4','9':'7',
              '43':'10','44':'13','45':'16',
              '10':'48','13':'47','16':'46',
              '48':'36','47':'33','46':'30',
              '36':'43','33':'44','30':'45'},
        'R':{ '10':'12','11':'15','12':'18',
              '13':'11','15':'17',
              '16':'10','17':'13','18':'16',
              '45':'19','42':'22','39':'25',
              '19':'54','22':'51','25':'48',
              '54':'9','51':'6','48':'3',
              '9':'45','6':'42','3':'39'},
        'B':{ '19':'21','20':'24','21':'27',
              '22':'20','24':'26',
              '25':'19','26':'22','27':'25',
              '39':'28','38':'31','37':'34',
              '28':'52','31':'53','34':'54',
              '52':'18','53':'15','54':'12',
              '18':'39','15':'38','12':'37'},
        'L':{ '28':'30','29':'33','30':'36',
              '31':'29','33':'35',
              '34':'28','35':'31','36':'34',
              '37':'1','40':'4','43':'7',
              '1':'46','4':'49','7':'52',
              '46':'27','49':'24','52':'21',
              '27':'37','24':'40','21':'43'},
        'U':{ '37':'39','38':'42','39':'45',
              '40':'38','42':'44',
              '43':'37','44':'40','45':'43',
              '21':'12','20':'11','19':'10',
              '12':'3','11':'2','10':'1',
              '3':'30','2':'29','1':'28',
              '30':'21','29':'20','28':'19'},
        'D':{ '46':'48','47':'51','48':'54',
              '49':'47','51':'53',
              '52':'46','53':'49','54':'52',
              '7':'16','8':'17','9':'18',
              '16':'25','17':'26','18':'27',
              '25':'34','26':'35','27':'36',
              '34':'7','35':'8','36':'9'} 
    }   
    
    def __init__(self, parms):
        #self.valid_operations = 'FfRrBbLlUuDd'
        self.orig_parms = parms
        self.solution = ""

        if (parms.get('cube') == None):
            raise AttributeError('No encoded cube string present')
        else: 
            self.cube_state = parms.get('cube')
            self.operation = parms.get('rotate')
            self.solve_flag = False
            
        if ((self.operation == None) or (self.operation == '')):
            self.solve_flag = True
# methods

# get cube string
    def getCube(self):
        return self.cube_state

# get valid cube status (boolean)
    def _isValidCube(self):
        result = check._check(self.orig_parms)
        if result.get('status') == 'ok':
            return True    
        else:
            return False
        
    def _isRotationValid(self):
        if ( (self.operation == None) or 
             (type(self.operation) != str) or (self.operation == '')):
            return False
        elif (not self._check_rotate_operation()):
            return False
        else:
            return True

    def _check_rotate_operation(self):
        for c in self.operation:
            if c not in self.valid_operations:
                return False
        return True

# rotate(move)
    def _rotate(self):
        if (self._isValidCube() and self._isRotationValid()):
            for op in self.operation:
                newEncoding = list(self.cube_state)
                assoc_map = self.rotation_map.get(op.upper())
                for sqr in assoc_map.keys():
                    sqrnum = int(sqr) - 1
                    if op.isupper():
                        newEncoding[int(assoc_map[sqr])-1] = self.cube_state[sqrnum]
                    else:
                        newEncoding[sqrnum] = self.cube_state[int(assoc_map[sqr])-1]
                self.cube_state = ''.join(newEncoding)
        return self.cube_state  
                
    def _getTopDaisyMiddle(self):
        # Middle color 
        if (self._isValidCube()):
            return self.cube_state[40]
        
    def _moveSequence(self, sequence):  
        for ch in sequence:
            self.operation = ch
            self._rotate()
            
    def _solveTopDaisySolution(self):
        solutionString = self._flipTopLayerEdges()
        #print(f"Cube after first top flip: {self.cube_state} ({solutionString})")
        
        solutionString = solutionString + self._daisyMiddleLayer()
        #print(f"Cube after middle layer: {self.cube_state} ({solutionString})")
        if self._isFlippedTopEdgePhaseOne():
            solutionString = solutionString + self._flipTopLayerEdges()
        #print(f"Cube after middle flip: {self.cube_state} ({solutionString})")
        #solutionString = self._flipBottomLayerEdges() #untested
        
        solutionString = solutionString + self._daisyBottomLayer()
        #print(f"Cube after bottom layer: {self.cube_state} ({solutionString})")
        # if self._isFlippedTopEdgePhaseOne():
        #     solutionString = solutionString + self._flipTopLayerEdges()
        
        if self._hasMiddleLayerPhaseOne():
            solutionString = solutionString + self._daisyMiddleLayer()
            
        if self._isFlippedTopEdgePhaseOne():
            solutionString = solutionString + self._flipTopLayerEdges()
        #print(f"Cube after last flip: {self.cube_state} ({solutionString})")

        #2 bottom layer
        self.solution = self.solution + solutionString
        return solutionString

    def _solveDownCrossSolution(self):
        solutionString = ""
        solutionStringBuilder = ""
        bottomMid = self.cube_state[49]
        keys = list(self.face_map.keys());
        topSequence = [43, 41, 37, 39]
        increment = 9
        beginEdge = 1
        beginMiddle = 4 
        
        if self._isTopDaisy():
            for r in range(0,4):
                solutionStringBuilder = ""
                edge = (increment * r) + beginEdge
                mid = (increment * r) + beginMiddle
                top = topSequence[r]
                #print(f"Face {keys[r]} of cube {self.cube_state}")
                #print(f"Comparing edge {edge}: {self.cube_state[edge]} and mid {mid}: {self.cube_state[mid]}")
                #print(f"Top edge is {self.cube_state[top]}")
                while self.cube_state[edge] != self.cube_state[mid] or self.cube_state[top] != bottomMid:
                    #print("Need to rotate, not a proper move")
                    solutionStringBuilder = solutionStringBuilder + 'U'
                    self.operation = 'U'
                    self._rotate()
                solutionStringBuilder = solutionStringBuilder + keys[r] + keys[r]
                #print(f"Builder for this face is {solutionStringBuilder}")
                self.operation = "" + keys[r] + keys[r]
                self._rotate()
                solutionString = solutionString + solutionStringBuilder
                #print(f"Solution is now {solutionString}")
        #print(f"Cube after down cross: {self.cube_state}")
        #print(f"Final solution: {solutionString}")
        self.solution = self.solution + solutionString
        return solutionString
    
    def _solveBottomLayerSolution(self):
        solutionString = ""
        #Step 1 - move incorrect corner placements on bottom
        #print(f"_solveBottomLayerSolution start: {self.solution}")
        if self._isBottomCross():
            solutionString = self._moveBottomCornerIncorrectPlacements()
            #print(f"_solveBottomLayerSolution 1 (move bad corners to top layer): {solutionString}")
            if (not self._isBottomCornerPlacementCorrect()):
                print(f"ERROR: Attempting to perform final bottom layer moves in bad state")
            #Step 2 - rotate up face until associated colors match adjacent faces
            solutionString = solutionString + self._moveTopCornersToCorrectColorAdj()
            #print(f"_solveBottomLayerSolution 2 (move to final pos): {solutionString}")

        self.solution = self.solution + solutionString
        #print(f"_solveBottomLayerSolution end: {self.solution}")
        if not self._isBottomComplete():
            print(f"ERROR: _solveBottomLayerSolution (Did not solve the layer!)")
            
        return solutionString
    
    def _solveMiddleLayerSolution(self):
        solutionString = ""
        if self._isBottomComplete():
            for face in range(0,4):
                solutionString = solutionString + self._positionTopEdgeToMiddleLayer(face)
        
        if not self._isMiddleLayerComplete():
            print(f"ERROR: _solveMiddleLayerSolution (Did not solve the layer!)")
            print(f"{solutionString} {self.cube_state}")
        else:
            print(f"SOLVED THE MIDDLE!! {solutionString} {self.cube_state}")    
        self.solution = self.solution + solutionString
        return solutionString
    
    def _daisyMiddleLayer(self):
        bottomMid = self.cube_state[49]
        solutionString = ""    
        while self._hasMiddleLayerPhaseOne():    
            for k in list(self.face_map.keys()):
                if k == 'U' or k == 'D':
                    pass
                else:
                    if k == 'F':
                        while (self.cube_state[3] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[39] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'l'
                            self.operation = 'l'
                            self._rotate()
                        while (self.cube_state[5] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[41] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'R'
                            self.operation = 'R'
                            self._rotate()
                    if k == 'R':
                        while (self.cube_state[12] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[43] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'f'
                            self.operation = 'f'
                            self._rotate()
                        while (self.cube_state[14] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[37] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'B'
                            self.operation = 'B'
                            self._rotate()
                    if k == 'B':
                        while (self.cube_state[21] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[41] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'r'
                            self.operation = 'r'
                            self._rotate()
                        while (self.cube_state[23] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[39] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'L'
                            self.operation = 'L'
                            self._rotate()
                    if k == 'L':
                        while (self.cube_state[30] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[37] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'b'
                            self.operation = 'b'
                            self._rotate()
                        while (self.cube_state[32] == bottomMid):
                            solutionStringBuilder = ""
                            while (self.cube_state[43] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'F'
                            self.operation = 'F'
                            self._rotate()
        return solutionString
    
    def _hasMiddleLayerPhaseOne(self):
        # 3, 5, 12, 14, 21, 23, 30, 32 are the middle layer locations on each side face
        bottomMid = self.cube_state[49]
        if (self.cube_state[3] == bottomMid or
            self.cube_state[5] == bottomMid or
            self.cube_state[12] == bottomMid or
            self.cube_state[14] == bottomMid or
            self.cube_state[21] == bottomMid or
            self.cube_state[23] == bottomMid or
            self.cube_state[30] == bottomMid or
            self.cube_state[32] == bottomMid):
            return True
        else:
            return False 
    
    def _daisyBottomLayer(self):
        solutionString = ""
        solutionStringBuilder = ""
        bottomMid = self.cube_state[49]
        
        while self._hasBottomLayerPhaseOne():
            for k in list(self.face_map.keys()):
                if k == 'U' or k == 'D':
                    pass
                else:
                    if k == 'F':
                        while (self.cube_state[7] == bottomMid or self.cube_state[46] == bottomMid):
                            solutionStringBuilder = ""
                            if self._isFlippedTopEdgePhaseOne():
                                solutionStringBuilder = solutionStringBuilder + self._flipTopLayerEdges()
                            while (self.cube_state[43] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'FF'
                            self.operation = 'FF'
                            self._rotate()   
                    if k == 'R':
                        while (self.cube_state[16] == bottomMid or self.cube_state[50] == bottomMid):
                            solutionStringBuilder = ""
                            if self._isFlippedTopEdgePhaseOne():
                                solutionStringBuilder = solutionStringBuilder + self._flipTopLayerEdges()
                            while (self.cube_state[41] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'RR'
                            self.operation = 'RR'
                            self._rotate()  
                    if k == 'B':
                        while (self.cube_state[25] == bottomMid or self.cube_state[52] == bottomMid):
                            solutionStringBuilder = ""
                            if self._isFlippedTopEdgePhaseOne():
                                solutionStringBuilder = solutionStringBuilder + self._flipTopLayerEdges()
                            while (self.cube_state[37] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'BB'
                            self.operation = 'BB'
                            self._rotate() 
                    if k == 'L':
                        while (self.cube_state[34] == bottomMid or self.cube_state[48] == bottomMid):
                            solutionStringBuilder = ""
                            if self._isFlippedTopEdgePhaseOne():
                                solutionStringBuilder = solutionStringBuilder + self._flipTopLayerEdges()
                            while (self.cube_state[39] == bottomMid):
                                solutionStringBuilder = solutionStringBuilder + "u"
                                self.operation = 'u'
                                self._rotate()
                            solutionString = solutionString + solutionStringBuilder + 'LL'
                            self.operation = 'LL'
                            self._rotate() 
        return solutionString
    
    def _hasBottomLayerPhaseOne(self):
        # 7, 16, 25, 34, 46, 48, 50, 52 are the bottom layer locations on each side face
        bottomMid = self.cube_state[49]
        if (self.cube_state[7] == bottomMid or
            self.cube_state[16] == bottomMid or
            self.cube_state[25] == bottomMid or
            self.cube_state[34] == bottomMid or
            self.cube_state[46] == bottomMid or
            self.cube_state[48] == bottomMid or
            self.cube_state[50] == bottomMid or
            self.cube_state[52] == bottomMid):
            return True
        else:
            return False 
        
    def _flipTopLayerEdges(self):
        solutionString = ""
        solutionStringBuilder = ""
        bottomMid = self.cube_state[49]
        keys = list(self.face_map.keys());
        edge = 1
        while self._isFlippedTopEdgePhaseOne() and edge < 54:
            #print(f"Cube state: {self.cube_state}")
            for itr in range(0,4):
                face = math.floor(edge / 9)
                #print(f"Edge is {edge}, face is {face}, r is {r}, cube is {self.cube_state}")
                if (self.cube_state[edge] == bottomMid):
                    #print(f"Edge match at {edge}, face {face}")
                    #face = math.floor(edge / 9) - 1
                    left = face - 1
                    if left < 0:
                        left = abs(face - 3)
                    solutionStringBuilder = ""
                    solutionStringBuilder = solutionStringBuilder + keys[face].lower()
                    solutionStringBuilder = solutionStringBuilder + 'U'
                    solutionStringBuilder = solutionStringBuilder + keys[left].lower()
                    solutionString = solutionString + solutionStringBuilder
                    break
                edge = edge + 9 #refactor with var
            self.operation = solutionStringBuilder
            self._rotate()
            #print(f"After rotate ({solutionStringBuilder}): {self.cube_state}")
            edge = 1
        return solutionString
    
    def _flipBottomLayerEdges(self):
        solutionString = ""
        solutionStringBuilder = ""
        bottomMid = self.cube_state[49]
        keys = list(self.face_map.keys());
        edge = 1
        while self._isFlippedTopEdgePhaseOne():
            for key in keys:
                face = math.floor(edge / 9)
                if (self.cube_state[edge] == bottomMid):
                    #face = math.floor(edge / 9) - 1
                    left = face - 1
                    if left < 0:
                        left = abs(face - 3)
                        solutionStringBuilder = ""
                        solutionStringBuilder = solutionStringBuilder + keys[face].lower()
                        solutionStringBuilder = solutionStringBuilder + 'U'
                        solutionStringBuilder = solutionStringBuilder + keys[left].lower()
                        solutionString = solutionString + solutionStringBuilder
                        break
                edge = edge + 9 #refactor with var
            self.operation = solutionStringBuilder
            self._rotate()
        return solutionString  
              
    def _isFlippedTopEdgePhaseOne(self):
        # 1, 10, 19, 28 are the top edge locations on each side face
        bottomMid = self.cube_state[49]
        if (self.cube_state[1] == bottomMid or
            self.cube_state[10] == bottomMid or
            self.cube_state[19] == bottomMid or
            self.cube_state[28] == bottomMid):
            return True
        else:
            return False
        
    def _isFlippedBottomEdgePhaseOne(self):
        # 46, 48, 50, 52 are the bottom edge locations with potential bottom color
        bottomMid = self.cube_state[49]
        result = False
        for r in range(46,53,2):
            if (self.cube_state[r] == bottomMid):
                result = True
        return result

    def _isBottomCross(self):
        bottomMid = self.cube_state[49]
        if (self.cube_state[46] == bottomMid and self.cube_state[48] == bottomMid and 
            self.cube_state[50] == bottomMid and self.cube_state[52] == bottomMid and 
            self.cube_state[4] == self.cube_state[7] and self.cube_state[13] == self.cube_state[16] and
            self.cube_state[22] == self.cube_state[25] and self.cube_state[31] == self.cube_state[34]):
            return True
        else:
            return False  
        

    
    def _isBottomCornerPlacementCorrect(self): #check if corner contains bottom color and should flip
        bottomFace = self.face_map.get('D')         
        bottomAdjDict = self.faceAdjMap.get('D')
        count = 0
        for sqr in bottomFace: # real numbers of bottom face
            if count in self.faceCorners:   # is this square a corner
                sqrAdjList = bottomAdjDict.get(sqr)
                adjCopy = sqrAdjList.copy()
                adjCopy.append(sqr)
                
                if self._doesAssociationContainColor(self._getMiddleColor(sqr), adjCopy):
                    midColors = self._getMiddleColorsForAdjList(adjCopy)
                    for adj in adjCopy:
                        if self.cube_state[adj] not in midColors:
                        # face = math.floor(adj / 9)     #determine face that sqr belongs to
                        # faceMid = (face * self.faceIncrement) + self.midIncrement # get middle color for that face
                        # if self.cube_state[faceMid] != self.cube_state[adj]:
                            #print(f"{self.cube_state[faceMid]} on {faceMid} does not match {self.cube_state[adj]} on {adj}")
                            return False #compare two colors
            count = count + 1
        return True      
    
    def _moveBottomCornerIncorrectPlacements(self): #Part 1 of Step 3 (solving bottom corners)
        bottomFace = self.face_map.get('D')
        bottomMid = self.cube_state[49]
        turnOrder = ['L','F','R','B']
        bottomAdjDict = self.faceAdjMap.get('D')
        solutionString = ""
        solutionStringBuilder = ""
   
        for itr in range(0,4):  # Look at each cube corner on the bottom and fix before moving on
            face = bottomFace[self.faceCorners[itr]]
            adjCopy = bottomAdjDict.get(face).copy()
            adjCopy.append(face)
            midColors = self._getMiddleColorsForAdjList(adjCopy)
            adjColors = self._getColorComboForAdjList(adjCopy)
            while bottomMid in adjColors and not set(adjColors).issubset(midColors):
                solutionStringBuilder = ""
                solutionStringBuilder = solutionStringBuilder + turnOrder[itr].lower()                 
                solutionStringBuilder = solutionStringBuilder + 'u'
                solutionStringBuilder = solutionStringBuilder + turnOrder[itr].upper()
                self._moveSequence(solutionStringBuilder)
                solutionString = solutionString + solutionStringBuilder
                adjColors = self._getColorComboForAdjList(adjCopy)
        return solutionString      
    
    def _doesAssociationContainColor(self, color, assocList):
        for item in assocList:
            if self.cube_state[item] == color:
                # print(f"item {item} color {self.cube_state[item]}")
                # print(f"list {list}")
                return True
        return False   
    
    def _moveTopCornersToCorrectColorAdj(self): # Part 3 of Step 3 (bottom layer)
        bottomMid = self.cube_state[49]
        turnOrder = ['F','R','B','L'] # cube is considered upside down
        solutionString = ''
        while self._isBottomColorInTopCorners():
            for face in range(0,4): #iterate for each corner / itr is the current face
                solutionStringBuilder = ''
                corner = face * self.faceIncrement
                adjList = self._getAdjacencyListBySquare(corner)
                adjCopy = adjList.copy()
                adjCopy.append(corner)
                adjCopy.sort()

                right = self._getFaceRightFlippedOrientation(face)
                midColors = []
                midColors.append(self._getMiddleColorByFace(face))
                midColors.append(self._getMiddleColorByFace(right))
                midColors.append(bottomMid)
                
            #if (self._isBottomColorInTopCorners()):
                #print(f"Calling Top Rotation with adjCopy {adjCopy} and midColors {midColors}")
                solutionStringBuilder = self._getTopRotationForBottomLayerPositionMatch(adjCopy, midColors)
                if solutionStringBuilder != '':
                    self._moveSequence(solutionStringBuilder)
                    solutionString = solutionString + solutionStringBuilder
                if self._doesTopCornerMatchBottomColorAdj(self._getColorComboForAdjList(adjCopy), midColors):
                    #print(f"Color match at {adjCopy}: {self._getColorComboForAdjList(adjCopy)} {midColors}")
                    #if white on top, flip to side
                    if self._isBottomColorOnTopSquare(adjCopy):
                        #flip sequence
                        flipSequence = turnOrder[face].upper() + 'u' + turnOrder[face].lower() + 'UU'
                        self._moveSequence(flipSequence)
                        solutionString = solutionString + flipSequence
                        
                    #test code, remove after done
                    if bottomMid not in [self.cube_state[adjCopy[0]],self.cube_state[adjCopy[1]]]:
                        print(f"ERROR: ROTATING A WRONG CORNER!!!!!!")
                    # end test code
 ### GOOD UP TO HERE 
                        
                    #adjCopy.sort()
                    #print(f"Check face {face} and right {right}")
                    #print(f"Turn order face {turnOrder[face]}, turn order right {turnOrder[right]}")
                    sequence = ''
                    if right > face: # corner of faces F and L
                        if self.cube_state[adjCopy[0]] == bottomMid:  #white is on right corner of front face
                            sequence = 'u' + turnOrder[right].lower() + 'U' + turnOrder[right].upper()
                        else:
                            sequence = 'U' + turnOrder[face].upper() + 'u' + turnOrder[face].lower()
                    else: #normal case for remaining three faces
                        if self.cube_state[adjCopy[0]] == bottomMid: #white is on left corner of right face
                            sequence = 'U' + turnOrder[face].upper() + 'u' + turnOrder[face].lower()
                        else:
                            sequence = 'u' + turnOrder[right].lower() + 'U' + turnOrder[right].upper()
                    self._moveSequence(sequence)
                    solutionString = solutionString + sequence
        #print(f'final solution: {solutionString}')
        #print(f'cube: {self.cube_state}')
        return solutionString

    def _isBottomColorOnTopSquare(self, myList):
        bottomMid = self.cube_state[49]
        for num in myList:
            color = self.cube_state[num]
            if bottomMid == color and num > 35:
                return True
        return False
            
    def _isBottomColorInTopCorners(self):
        faceList = list(self.face_map.keys())
        bottomMid = self.cube_state[49]
        for itr in range(0,4): #iterate for each corner / itr is the current face
            corner = itr * self.faceIncrement
            face = self._getFaceOfSquare(corner)
            adjList = self.faceAdjMap.get(faceList[face]).get(corner)
            adjCopy = adjList.copy()
            adjCopy.append(corner)
            #right = face - 1 if (face - 1) >= 0 else abs(face - 3) #face to right of flipped cube
            adjColors = self._getColorComboForAdjList(adjCopy)
            if (bottomMid in adjColors):
                return True
        return False
#<!--START NEW CODE A6   
    def _getTopRotationForBottomLayerPositionMatch(self, adjList, midColors):
        # This function gets the middle face colors for a top corner to see if it is position to rotate to 
        # the bottom layer as part of phase 3
        solutionSequence = ''
        rotationCount = 0
        while rotationCount < 4: # 4 rotations puts us back to original starting pos
            adjColors = self._getColorComboForAdjList(adjList)
            #print(f'Rotations made: {rotationCount}')
            #print(f"Checking if {adjColors} matches {midColors}")
            if set(adjColors).issubset(midColors):
                #We have a match
                #print(f"Corner match {adjColors}")
                #print(f"Solution sequence is {solutionSequence}")
                self._moveSequence(solutionSequence.lower()) #put top layer back to original state
                adjColors = self._getColorComboForAdjList(adjList)
                #print(f"Reset cube state, corner colors are now {adjColors} again")
                return solutionSequence
            else: 
                #rotate top and test again
                self._moveSequence('U')
                solutionSequence = solutionSequence + 'U'
                rotationCount = rotationCount + 1
        if rotationCount == 4:
            # back where we started with no match, no need to add UUUU to solution, so reset it
            # corner must already be in place on bottom layer
            return ''    
    
    def _doesTopCornerMatchBottomColorAdj(self, adjColors, bottomMidColors):
        if set(adjColors).issubset(bottomMidColors):
            return True
        else:
            return False
        
#--> END NEW CODE A6
    
    def _getSideAdjacencies(self, myList):
        newList = []
        for adj in myList:
            if adj < 36:
                newList.append(adj)
        return newList
    
    def _getFaceOfSquare(self, square):        
        return math.floor(square / self.faceIncrement)

    def _getMiddleColor(self, facePosition):
        face = self._getFaceOfSquare(facePosition)
        faceMid = (face * self.faceIncrement) + self.midIncrement # get middle color for that face
        return self.cube_state[faceMid]
    
    def _getMiddleColorByFace(self, facePosition):
        faceMid = (facePosition * self.faceIncrement) + self.midIncrement # get middle color for that face
        return self.cube_state[faceMid]
    
    def _getMiddleColorsForAdjList(self, adjList):
        newList = []
        for sqr in adjList:
            newList.append(self._getMiddleColor(sqr))
        return newList
    
    def _getColorComboForAdjList(self, adjList):
        newList = []
        for sqr in adjList:
            newList.append(self.cube_state[sqr])
        return newList

    def _getAdjacencyListBySquare(self, square):
        faceList = list(self.face_map.keys())
        adjList = self.faceAdjMap.get(faceList[self._getFaceOfSquare(square)]).get(square)
        return adjList
    
    def _isTopDaisy(self):
        bottomMid = self.cube_state[49]
        if (self.cube_state[37] == bottomMid and self.cube_state[39] == bottomMid and 
            self.cube_state[41] == bottomMid and self.cube_state[43] == bottomMid):
            return True
        else:
            return False      
 
    def _isBottomComplete(self):
        bottomMid = self.cube_state[49]
        for square in range(45,54):
            if self.cube_state[square] != bottomMid:
                return False
## <-- START NEW FOR A6
        for face in range(0,4):
            for offset in range(6,9):
                if self.cube_state[face * self.faceIncrement + offset] != self._getMiddleColorByFace(face):
                    return False
        return True
    
    def _isMiddleLayerComplete(self):
        for face in range(0,4):
            midColor = self._getMiddleColorByFace(face)
            midLeft = (face * self.faceIncrement) + self.midIncrement - 1
            midRight = (face * self.faceIncrement) + self.midIncrement + 1
            if midColor != self.cube_state[midLeft] or midColor != self.cube_state[midRight]:
                return False
            return True
    
    def _isTopComplete(self):
        topMid = self.cube_state[40]
        for square in range(36,45):
            if self.cube_state[square] != topMid:
                return False
        for face in range(0,4):
            for offset in range(0,3):
                if self.cube_state[face * self.faceIncrement + offset] != self._getMiddleColorByFace(face):
                    return False
        return True
    
    def _isCubeSolved(self):
        if self._isBottomComplete() and self._isMiddleLayerComplete() and self._isTopComplete():
            return True
        else:
            return False

    def _isSideFaceMiddleVerticalMatched(self, face):
        if face < 0 or face > 3:
            return False
        sideMatch = False
        midColor = self._getMiddleColorByFace(face)
        midTop = (face * self.faceIncrement) + self.midIncrement - 3
        midBottom = (face * self.faceIncrement) + self.midIncrement + 3
        edgeAdjList = self._getAdjacencyListBySquare(midTop)
        edgeAdjColors = self._getColorComboForAdjList(edgeAdjList)
        
        sidefaceAdjColors = self._getSideFaceAdjacencyMiddleColors(face)
        for edgeColor in edgeAdjColors:
            if edgeColor in sidefaceAdjColors:
                sideMatch = True
        
        if sideMatch and midColor == self.cube_state[midTop] and midColor == self.cube_state[midBottom]:
            return True
        else:
            return False       
    
    def _getSideFaceAdjacencyMiddleColors(self, face):
        #returns a list of middle colors for each side adjacent to the current face
        faceLeft = self._getFaceLeftNormalOrientation(face)
        faceRight = self._getFaceRightNormalOrientation(face)
        sideAdjColors = [self._getMiddleColorByFace(faceLeft),self._getMiddleColorByFace(faceRight)]
        return sideAdjColors
    
    def _getFaceRightEdgeSquare(self, face):
        rightEdge = (face * self.faceIncrement) + self.rightEdgeIncrement
        return rightEdge

    def _getFaceLeftEdgeSquare(self, face):
        leftEdge = (face * self.faceIncrement) + self.leftEdgeIncrement
        return leftEdge
    
    def _getFaceTopEdgeSquare(self, face):
        topEdge = (face * self.faceIncrement) + self.topEdgeIncrement
        return topEdge
    
    def _getFaceBottomEdgeSquare(self, face):
        bottomEdge = (face * self.faceIncrement) + self.bottomEdgeIncrement
        return bottomEdge
    
    def _isRightEdgePlacementCorrectForFace(self, face):
        topMid = self._getMiddleColorByFace(4)
        edge = self._getFaceRightEdgeSquare(face)
        edgeAdjList = self._getAdjacencyListBySquare(edge)
        edgeAdjCopy = edgeAdjList.copy()
        edgeAdjCopy.append(edge)
        edgeAdjColors = self._getColorComboForAdjList(edgeAdjCopy)
        sideAdjColors = self._getMiddleColorsForAdjList(edgeAdjList)
        if set(edgeAdjColors).issubset(sideAdjColors) and topMid not in edgeAdjColors:
            return True
        else:
            return False
 
    def _areEdgeColorsInSideEdgeColorPairings(self, edgeAdjColors):
        print(f"{edgeAdjColors} in {self._getSideFaceColorPairings()}")
        sidePairings = self._getSideFaceColorPairings()
        for pairing in sidePairings:
            if set(edgeAdjColors).issubset(pairing):
        #if edgeAdjColors in self._getSideFaceColorPairings():
                return True
        return False
    
    def _isRightEdgeMismatchedForMiddleLayer(self, face, edgeAdjList):
        edgeAdjColors = self._getColorComboForAdjList(edgeAdjList)
        print(f"edge mismatch: {edgeAdjList} {edgeAdjColors}")
        if self._areEdgeColorsInSideEdgeColorPairings(edgeAdjColors) and not self._isRightEdgePlacementCorrectForFace(face):
            return True
        else:
            return False
    
    def _getFaceLeftNormalOrientation(self, face):
        faceLeft = face - 1 if (face - 1) >= 0 else abs(face - 3) #face to right of flipped cube
        return faceLeft
        
    def _getFaceRightNormalOrientation(self, face):
        faceRight = face + 1 if (face + 1) <= 3 else 0 #face to right of flipped cube
        return faceRight

    def _getFaceLeftFlippedOrientation(self, face):
        faceLeft = face + 1 if (face + 1) <= 3 else 0 #face to left of flipped cube
        return faceLeft
    
    def _getFaceRightFlippedOrientation(self, face):
        faceRight = face - 1 if (face - 1) >= 0 else abs(face - 3) #face to right of flipped cube
        return faceRight
        
    def _getSideFaceColorPairings(self):
        # returns a list of lists containing each color pairing of side faces, 4 total
        colorPairings = []
        colorPairingSingle = []
        for face in range(0,4):
            colorPairingSingle.append(self._getMiddleColorByFace(face))
            colorPairingSingle.append(self._getMiddleColorByFace(self._getFaceRightNormalOrientation(face)))
            colorPairings.append(colorPairingSingle)
            colorPairingSingle = []            
        return colorPairings
    
    def _getRightEdgeSideFaceColorPairingByFace(self, face):
        colorPairing = []
        colorPairing.append(self._getMiddleColorByFace(face))
        colorPairing.append(self._getMiddleColorByFace(self._getFaceRightNormalOrientation(face)))
        return colorPairing

    def _getLeftEdgeSideFaceColorPairingByFace(self, face):
        colorPairing = []
        colorPairing.append(self._getMiddleColorByFace(face))
        colorPairing.append(self._getMiddleColorByFace(self._getFaceLeftNormalOrientation(face)))
        return colorPairing
        
    def _getTargetForMiddleLayerFinalSequence(self, face):
        #return left or right
        target = None
        if self._isSideFaceMiddleVerticalMatched(face):
            topEdge = self._getFaceTopEdgeSquare(face)
            topEdgeAdjList = self._getAdjacencyListBySquare(topEdge)
            topEdgeAdjCopy = topEdgeAdjList.copy()
            topEdgeAdjCopy.append(topEdge)
            topEdgeAdjColors = self._getColorComboForAdjList(topEdgeAdjCopy)  
            
            rightAdjColors = self._getRightEdgeSideFaceColorPairingByFace(face)
            leftAdjColors = self._getLeftEdgeSideFaceColorPairingByFace(face)
                         
            if set(topEdgeAdjColors).issubset(rightAdjColors):
                target = self._getFaceRightNormalOrientation(face)
            elif set(topEdgeAdjColors).issubset(leftAdjColors):
                target = self._getFaceLeftNormalOrientation(face)
            
            print(f"TARGET: {target}")
            print(f"{topEdgeAdjColors} -> {rightAdjColors}")
            print(f"{topEdgeAdjColors} -> {leftAdjColors}")

        return target
        
        
    def _rotateToMiddleVerticalLineOnSideFace(self, face):
        solutionString = ''
        sequenceBuilder = ''
        attempts = 0
        while attempts < 4:
            sequence = 'U'
            self._moveSequence(sequence)
            sequenceBuilder = sequenceBuilder + sequence
            attempts = attempts + 1
            if self._isSideFaceMiddleVerticalMatched(face):
                break
        
        if sequenceBuilder == 'UUUU':
            solutionString = ''
        else:
            solutionString = sequenceBuilder
        return solutionString  
    
    def _rotateRightForMiddleLayer(self, face, faceRight):
        faces = list(self.face_map.keys())
        front = faces[face]
        right = faces[faceRight]
        sequence = 'U' + right + 'u' + right.lower() + 'u' + front.lower() + 'U' + front
        print(f"faces{faces} front{front} right{right}")
        self._moveSequence(sequence)
        return sequence
    
    def _rotateLeftForMiddleLayer(self, face, faceLeft):
        faces = list(self.face_map.keys())
        front = faces[face]
        left = faces[faceLeft]
        sequence = 'u' + left.lower() + 'U' + left + 'U' + front + 'u' + front.lower()
        print(f"faces{faces} front{front} left{left}")
        self._moveSequence(sequence)
        return sequence 
    
    def _positionTopEdgeToMiddleLayer(self, face):
        solutionString = ''
        while not self._isSideFaceMiddleVerticalMatched(face):
            # flip an edge in place
            sequence = self._rotateToMiddleVerticalLineOnSideFace(face)
            if sequence == '':
                #flip an edge
                for flipFace in range(0,4):
                    rightEdge = self._getFaceRightEdgeSquare(flipFace)
                    rightEdgeAdj = self._getAdjacencyListBySquare(rightEdge)
                    rightEdgeAdjCopy = rightEdgeAdj.copy()
                    rightEdgeAdjCopy.append(rightEdge)
                    if self._isRightEdgeMismatchedForMiddleLayer(flipFace, rightEdgeAdjCopy):
                        flipSequence = self._rotateRightForMiddleLayer(flipFace, self._getFaceRightNormalOrientation(flipFace))
                        sequence = sequence + flipSequence
                        break
            solutionString = solutionString + sequence
            
        if self._isSideFaceMiddleVerticalMatched(face):
            target = self._getTargetForMiddleLayerFinalSequence(face)
            if target == self._getFaceRightNormalOrientation(face):
                solutionString = solutionString + self._rotateRightForMiddleLayer(face, self._getFaceRightNormalOrientation(face))
            else:
                solutionString = solutionString + self._rotateLeftForMiddleLayer(face, self._getFaceLeftNormalOrientation(face))
            #found a new square to test
            
        return solutionString             
 ## <-- END NEW FOR A6
            
    def _getRandomScramble(self):
        ops = ""
        for _ in range(1,15):
            randAttempt = random.randrange(0,12)
            ops = ops + self.valid_operations[randAttempt]
        
        self.operation = ops
        self._rotate()
        return self.cube_state
                
    def _tryNeural(self):
        origCube = self.cube_state
        bottomMid = self.cube_state[49]
        count = 0
        randAttempt = 0
        solution = ""
        self.solution = solution
        if self._isBottomCross():
            return
        while(True):
            randAttempt = random.randrange(0,12)
            self.operation = self.valid_operations[randAttempt]
            solution = solution + self.operation
            self._rotate()
            if (self.cube_state[46] == bottomMid and self.cube_state[48] == bottomMid and 
                self.cube_state[50] == bottomMid and self.cube_state[52] == bottomMid):
                break
            else:
                count += 1
                if (count > 15):
                    count = 0
                    solution = ""
                    self.cube_state = origCube
        self.solution = solution            
                    
    def _tryNeuralFive(self):
        origCube = self.cube_state
        count = 0
        total = 0
        randAttempt = 0
        solution = ""
        if self._isMiddleLayerComplete():
            return
        while(True):
            randAttempt = random.randrange(0,12)
            self.operation = self.valid_operations[randAttempt]
            solution = solution + self.operation
            self._rotate()
            if self._isMiddleLayerComplete() and self._isBottomComplete():
                break
            else:
                count += 1
                if (count > 40):
                    total = total + count
                    count = 0
                    solution = ""
                    self.cube_state = origCube
        #self.solution = self.solution + solution 
        #return self.solution    
        return solution     
        
                    
    