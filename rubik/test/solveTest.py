# Brian Adair 
# COMP 6700 - Assignment 03
# 2022-02-24

# Tests of solve operations
import unittest
import rubik.solve as solve

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
#        confidence level: BVA
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
        
# Sad path tests
#    Analysis: test the error conditions that can occur with inputs using the solve module
#                - note: cube string validation checks are performed in the check module, and 
#                -       unit tested separately
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
        self.assertEqual(expectedResult, actualResult, 'Invalid cube state')
     
        

