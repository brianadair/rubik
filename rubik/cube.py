'''
    Created on ?
    @author: Brian Adair
    
'''
import rubik.check as check
import random
import math

class Cube:
    '''
    Rubik's cube
    '''
    valid_operations = 'FfRrBbLlUuDd'
    
    face_map = {
        'F': [1,2,3,4,5,6,7,8,9],
        'R': [10,11,12,13,14,15,16,17,18],
        'B': [19,20,21,22,23,24,25,26,27],
        'L': [28,29,30,31,32,33,34,35,36],
        'U': [37,38,39,40,41,42,43,44,45],
        'D': [46,47,48,49,50,51,52,53,54]
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
#New code A4    
    def _getTopDaisyMiddle(self):
        # Middle color 
        if (self._isValidCube()):
            return self.cube_state[40]
# NEW CODE A5
    def _solveTopDaisySolution(self):
        #1 middle layer
        bottomMid = self.cube_state[49]
        #solutionString = ""
        solutionString = self._flipTopLayerEdges()
        solutionString = solutionString + self._daisyMiddleLayer()
        #solutionString = self._flipBottomLayerEdges() #untested
        solutionString = solutionString + self._daisyBottomLayer()
        print(f"Cube is {self.cube_state}")
        solutionString = solutionString + self._flipTopLayerEdges()
        #2 bottom layer
        return solutionString
    
    def _daisyMiddleLayer(self):
        bottomMid = self.cube_state[49]
        solutionString = ""        
        for k in self.face_map.keys():
            if k == 'U' or k == 'D':
                pass
            else:
                if k == 'F':
                    if (self.cube_state[3] == bottomMid):
                        while (self.cube_state[39] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'l'
                        self.operation = 'l'
                        self._rotate()
                    if (self.cube_state[5] == bottomMid):
                        while (self.cube_state[41] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'R'
                        self.operation = 'R'
                        self._rotate()
                if k == 'R':
                    if (self.cube_state[12] == bottomMid):
                        while (self.cube_state[43] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'f'
                        self.operation = 'f'
                        self._rotate()
                    if (self.cube_state[14] == bottomMid):
                        while (self.cube_state[37] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'B'
                        self.operation = 'B'
                        self._rotate()
                if k == 'B':
                    if (self.cube_state[21] == bottomMid):
                        while (self.cube_state[41] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'r'
                        self.operation = 'r'
                        self._rotate()
                    if (self.cube_state[23] == bottomMid):
                        while (self.cube_state[39] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'L'
                        self.operation = 'L'
                        self._rotate()
                if k == 'L':
                    if (self.cube_state[30] == bottomMid):
                        while (self.cube_state[37] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'b'
                        self.operation = 'B'
                        self._rotate()
                    if (self.cube_state[32] == bottomMid):
                        while (self.cube_state[43] == bottomMid):
                            solutionString = solutionString + "u"
                            self.operation = 'u'
                            self._rotate()
                        solutionString = solutionString + 'F'
                        self.operation = 'F'
                        self._rotate()
        return solutionString
    
    def _daisyBottomLayer(self):
        solutionString = ""
        solutionStringBuilder = ""
        bottomMid = self.cube_state[49]
        
        for k in list(self.face_map.keys()):
            if k == 'F':
                if (self.cube_state[7] == bottomMid or self.cube_state[46] == bottomMid):
                    while (self.cube_state[43] == bottomMid):
                        solutionString = solutionString + "u"
                        self.operation = 'u'
                        self._rotate()
                    solutionString = solutionString + 'FF'
                    self.operation = 'FF'
                    self._rotate()   
            elif k == 'R':
                if (self.cube_state[16] == bottomMid or self.cube_state[48] == bottomMid):
                    while (self.cube_state[41] == bottomMid):
                        solutionString = solutionString + "u"
                        self.operation = 'u'
                        self._rotate()
                    solutionString = solutionString + 'RR'
                    self.operation = 'RR'
                    self._rotate()  
            elif k == 'B':
                if (self.cube_state[25] == bottomMid or self.cube_state[50] == bottomMid):
                    while (self.cube_state[37] == bottomMid):
                        solutionString = solutionString + "u"
                        self.operation = 'u'
                        self._rotate()
                    solutionString = solutionString + 'BB'
                    self.operation = 'BB'
                    self._rotate() 
            elif k == 'L':
                if (self.cube_state[34] == bottomMid or self.cube_state[52] == bottomMid):
                    while (self.cube_state[39] == bottomMid):
                        solutionString = solutionString + "u"
                        self.operation = 'u'
                        self._rotate()
                    solutionString = solutionString + 'LL'
                    self.operation = 'LL'
                    self._rotate() 
        return solutionString

    def _flipTopLayerEdges(self):
        solutionString = ""
        solutionStringBuilder = ""
        bottomMid = self.cube_state[49]
        keys = list(self.face_map.keys());
        edge = 1
        while self._isFlippedTopEdgePhaseOne():
            #for key in keys:
            for r in range(0,4):
                face = math.floor(edge / 9)
                print(f"Edge is {edge}, face is {face}")
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
    
# import line + 1
#END NEW CODE

    def _isTopDaisy(self):
        bottomMid = self.cube_state[49]
        if (self.cube_state[37] == bottomMid and self.cube_state[39] == bottomMid and 
            self.cube_state[41] == bottomMid and self.cube_state[43] == bottomMid):
            return True
        else:
            return False      
        
    def _isBottomCross(self):
        bottomMid = self.cube_state[49]
        if (self.cube_state[46] == bottomMid and self.cube_state[48] == bottomMid and 
            self.cube_state[50] == bottomMid and self.cube_state[52] == bottomMid):
            return True
        else:
            return False  
            
        
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
                    
        
        
                    
    