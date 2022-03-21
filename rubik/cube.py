import rubik.check as check
import random
from _ast import Or

class Cube:
    '''
    Rubik's cube
    '''
    valid_operations = 'FfRrBbLlUuDd'
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
            
        if ((self.operation == None) or (self.operation == '')):
            self.operation = 'F'
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
        
    def _isTopDaisy(self):
        bottomMid = self.cube_state[49]
        print(f"Bottom Mid is {bottomMid}")
        if (self.cube_state[37] == bottomMid and self.cube_state[39] == bottomMid and 
            self.cube_state[41] == bottomMid and self.cube_state[43] == bottomMid):
            return True
        else:
            return False       
            
        
    def _tryRandom(self):
        bottomMid = self.cube_state[49]
        print(f"Bottom Mid is {bottomMid}")
        count = 0
        randAttempt = 0
        solution = ""
        while(True):
            randAttempt = random.randrange(0,12)
            self.operation = self.valid_operations[randAttempt]
            solution = solution + self.operation
            self._rotate()
            if (self.cube_state[46] == bottomMid and self.cube_state[48] == bottomMid and 
                self.cube_state[50] == bottomMid and self.cube_state[52] == bottomMid):
                print(f"Success: {count} attempts")
                print(f"Cube: {self.cube_state}")
                print(f"Solution: {solution}")
                break
            else:
                print("Unsuccessful")
                count += 1
        
                    
    