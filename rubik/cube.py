import rubik.check as check
from _ast import Or

class Cube:
    '''
    Rubik's cube
    '''
    def __init__(self, parms):
        self.valid_operations = 'FfRrBbLlUuDd'
        if (parms.get('cube') != None):
            self.cube_state = parms.get('cube')
            self.orig_parms = parms
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
    