import rubik.cube as cube

def _solve(parms):
    result = {}
    cube_model = cube.Cube(parms)
    if cube_model._isValidCube():
        encodedCube = parms.get('cube',None)       #get "cube" parameter if present
        result['status'] = 'ok'
    return result