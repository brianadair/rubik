import rubik.check as check

class Cube:
    '''
    Rubik's cube
    '''
    def __init__(self, parms):
        self.valid_operations = 'FfRrBbLlUuDd'
        if (parms.get('cube') != None):
            self.cube_state = parms.get('cube')
            self.orig_parms = parms
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
        rotate_key = self.orig_parms['rotate']
        if (rotate_key == None):
            return False
        elif (type(rotate_key) != str):
            return False
        elif (not self._check_rotate_operation()):
            return False
        else:
            return True

    def _check_rotate_operation(self):
        rotate_key = self.orig_parms['rotate']
        print(f"Rotate key = {rotate_key}")
        for c in rotate_key:
            print(f"Operation: {c}")
            if c not in self.valid_operations:
                print(f"{c} is not a valid operation")
                return False
        return True

# rotate(move)
    