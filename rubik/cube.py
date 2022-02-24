class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, parms):
        if (parms.get('cube') != None):
            self.cube_state = parms.get('cube')
# methods
# get cube
    def getCube(self):
        return self.cube_state
# rotate(move)
