'''
    Created on ?
    @author: Brian Adair
    
'''
import rubik.cube as cube

def _solve(parms):
    result = {}
    try:
        cube_model = cube.Cube(parms)
    except AttributeError:
        result['status'] = 'error: no cube argument provided'
        return result    
    
    if not cube_model._isValidCube():
        #encodedCube = parms.get('cube',None)       #get "cube" parameter if present
        result['status'] = 'error: invalid cube state'
    elif cube_model.solve_flag == False and not cube_model._isRotationValid():
        result['status'] = 'error: invalid rotation'
    elif cube_model.solve_flag == True and cube_model._isCubeSolved():
        result['solution'] = ''
        result['status'] = 'ok'
        return result        
    elif cube_model.solve_flag == True:
        cube_model._solveTopDaisySolution()
        #print(f"Top Daisy solution: {cube_model.solution}")
        #print(f"Is Top Daisy? {cube_model._isTopDaisy()}")

        cube_model._solveDownCrossSolution()
        #print(f"Down Cross solution: {cube_model.solution}")
        #print(f"Is Bottom Cross? {cube_model._isBottomCross()}")


        cube_model._solveBottomLayerSolution()
        #print(f"Bottom Layer solution: {cube_model.solution}")
        #print(f"Is Bottom Complete? {cube_model._isBottomComplete()}")
        
        cube_model._solveMiddleLayerSolution()
        result['solution'] = cube_model.solution
        result['status'] = 'ok'
    else:
        result['cube'] = cube_model._rotate()
        result['status'] = 'ok'

    return result


