import rubik.check as check

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, parms):
        if (parms.get('cube') != None):
            self.cube_state = parms.get('cube')
            self.orig_parms = parms
# methods

# get cube string
    def getCube(self):
        return self.cube_state

# get valid cube status (boolean)
    def _isValidCube(self):    
        return False
# rotate(move)
    