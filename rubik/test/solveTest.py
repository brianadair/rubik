'''
    Created on ?
    @author: Brian Adair
    
'''
# Brian Adair 
# COMP 6700 - Assignment 03
# 2022-02-24

# Tests of solve operations
import unittest
import rubik.solve as solve
from rubik.cube import Cube

class SolveTest(unittest.TestCase):
# Analysis
#    _solve(parms):
#        inputs:
#            parms: dictionary, mandatory, validated
#                    key: 'op', string, mandatory, validated
#                    key: 'cube', string, mandatory, unvalidated
#                    key: 'rotate', string, optional (defaults to 'F'), unvalidated
#
#        outputs:
#            side-effects: cube string is potentially changed for the cube instance
#            returns: dictionary, contains two keys ('cube','status') 
#                     with the new cube state and the value of 'ok' when all conditions for a valid 
#                     cube are met, or an error message indicating the failed condition of the request. 
#
#        confidence level: BVA; for _solve, the boundary in this context is defined as a rotate operation
#                          not in the allowed set of characters, which are not in a range or sequence.
#                    
#
#
# Happy Path tests
#    test_010: cube validated before operations performed
#    test_020:
#    test_021:
#    test_022:
#    test_030:
#    test_040:
#    test_041:


    def test_010_ShouldPassValidCubeCheck(self):
        parm = {'op':'solve',
                'rotate': 'F',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        expectedResult = 'ok'
        actualResult = result.get('status')
        self.assertEqual(expectedResult, actualResult)
    
    def test_020_ShouldReturnOKOnRotateParamPresent(self):
        parm = {'op':'solve',
                'rotate': 'F',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        expectedResult = 'ok'
        actualResult = result.get('status')
        self.assertEqual(expectedResult, actualResult)
        
    def test_021_ShouldReturnOKOnRotateParamMissing(self):
        parm = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        expectedResult = 'ok'
        actualResult = result.get('status')
        self.assertEqual(expectedResult, actualResult)

    def test_022_ShouldReturnOKOnRotateParamEmptyString(self):
        parm = {'op':'solve',
                'rotate':'',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        expectedResult = 'ok'
        actualResult = result.get('status')
        self.assertEqual(expectedResult, actualResult)        
 
    def test_030_ShouldReturnOKOnRotateValidSymbols(self):
        parm = {'op':'solve',
                'rotate': 'FfRrBbLlUuDd',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        expectedResult = 'ok'
        actualResult = result.get('status')
        self.assertEqual(expectedResult, actualResult)
    
    def test_040_ShouldReturnCorrectEncodingOnDefaultRotation(self):
        parm = {'op':'solve',
                'rotate': 'F',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        actualResult = result.get('status')
        self.assertEquals(actualResult,'ok')
        actualResult = result.get('cube')
        expectedResult = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        self.assertEquals(expectedResult, actualResult,"incorrect rotation result")

    def test_041_ShouldReturnCorrectEncodingOnMultipleRotations(self):
        parm = {'op':'solve',
                'rotate': 'Fd',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        actualResult = result.get('status')
        self.assertEquals(actualResult,'ok')
        actualResult = result.get('cube')
        expectedResult = 'ggggggwrrwrrwrrbbbbbbbbbooyooyooygggwwwwwwoooryyryyryy'
        self.assertEquals(expectedResult, actualResult,"incorrect rotation result")
    
    @unittest.skip('Work on cube model')    
    def test_101_ShouldProduceBottomCrossFromRandomCubes(self):
        parm = {'op':'solve',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        test_cube = Cube(parm)
        for r in range(1,500):
            test_cube._getRandomScramble()
            cubeState = test_cube.cube_state
            randomParm = {'op':'solve',
                          'cube': cubeState}
            result = solve._solve(randomParm)
            actualResult = result.get('status')
            print(f"BOTTOM LAYER {r}: {cubeState} initialized")
            self.assertEquals(actualResult, 'ok')
            print(f"BOTTOM LAYER {r}: {result} {result.get('solution')}")

        # actualResult = False
        # expectedResult = True
        # self.assertEquals(expectedResult, actualResult,"incorrect solution result")        
    
    #@unittest.skip('Run after generating a random scrambled cube')
    def test_102_ShouldProduceBottomLayerSolution(self):
        parm = {'op':'solve',
                'cube':'wrgoggwgrryrwrobwobygwbybrgogbbogoorwoyyyrowygrwbwbyby'}
        result = solve._solve(parm)
        actualResult = result.get('status')
        print(f"SOLVE Test 102 solution: {result.get('solution')}")
        self.assertEquals(actualResult,'ok')
        
    
    def test_103_ShouldProduceBottomLayerFromRandomCubes(self):
        parm = {'op':'solve',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'}
        test_cube = Cube(parm)
        for r in range(1,50):
            test_cube._getRandomScramble()
            cubeState = test_cube.cube_state
            randomParm = {'op':'solve',
                          'cube': cubeState}
            result = solve._solve(randomParm)
            actualResult = result.get('status')
            print(f"BOTTOM LAYER {r}: {cubeState} initialized")
            self.assertEquals(actualResult, 'ok')
            print(f"BOTTOM LAYER {r}: {result} {result.get('solution')}")         
# Sad path tests
#    Analysis: test the error conditions that can occur with inputs using the solve module
#                - note: cube string validation checks are performed in the check module, and 
#                -       are unit tested separately
#    test_910: generate error on invalid rotation command
#    test_920: generate error on invalid cube string

    def test_910_ShouldErrorOnInvalidRotationCommand(self):
        parm = {'op':'solve',
                'rotate': 'Z',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        actualResult = result.get('status')
        expectedResult = 'error: invalid rotation'
        self.assertEquals(expectedResult, actualResult, "Invalid rotation command")
        
    def test_920_ShouldErrorOnInvalidCubeState(self):
        parm = {'op':'solve',
                'rotate': 'F',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4Wy4WWgWygWWg'}
        result = solve._solve(parm)
        actualResult = result.get('status')
        expectedResult = 'error: invalid cube state'
        self.assertEquals(expectedResult, actualResult, 'Invalid cube state')
        
    def test_930_ShouldErrorOnMissingCubeArgument(self):
        parm = {'op':'solve',
                'rotate': 'F'}
        result = solve._solve(parm)
        actualResult = result.get('status')
        expectedResult = 'error: no cube argument provided'
        self.assertEquals(expectedResult, actualResult)
