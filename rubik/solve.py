import rubik.cube as cube



def _solve(parms):
    result = {}
    cube_model = cube.Cube(parms)
    
    if not cube_model._isValidCube():
        #encodedCube = parms.get('cube',None)       #get "cube" parameter if present
        result['status'] = 'error: invalid cube'
    elif not cube_model._isRotationValid():
        result['status'] = 'error: request parm invalid data'
    else:
        result['status'] = 'ok'
    
    
    return result

