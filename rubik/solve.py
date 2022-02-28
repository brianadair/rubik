import rubik.cube as cube



def _solve(parms):
    result = {}
    cube_model = cube.Cube(parms)
    
    if not cube_model._isValidCube():
        #encodedCube = parms.get('cube',None)       #get "cube" parameter if present
        result['status'] = 'error: invalid cube state'
    elif not cube_model._isRotationValid():
        result['status'] = 'error: invalid rotation'
    else:
        result['cube'] = cube_model._rotate()
        result['status'] = 'ok'
    
    return result

