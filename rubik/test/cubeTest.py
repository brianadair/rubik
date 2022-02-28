# Brian Adair 
# COMP 6700 - Assignment 03
# 2022-02-24

# Tests of cube properties and methods

import unittest
from rubik.cube import Cube
from pickle import NONE


class Test(unittest.TestCase):
# Analysis
#    _cube(parms):
#        inputs:
#            parms: dictionary, mandatory, validated
#                    key: 'op', string, mandatory, validated
#                    key: 'cube', string, mandatory, unvalidated
#                    key: 'rotate', string, optional (defaults to 'F'), unvalidated
#
#        outputs:
#            side-effects: cube state is potentially changed (new encoded string)
#            returns: 
#                - string: getCube() returns the current cube state for the instance
#                - boolean: internal functions that validate request parameters and inputs
#                - string: _rotate() returns the new encoded string for the cube state 
#                          following the rotation
#
#        confidence level: BVA
#
#
# Happy path tests
#   test_010: Instantiate cube object
#   test_020: Assure cube_state property is set
#   test_030: valid cube instance returns the encoded cube string
#   test_040: successfully validates a cube
#   test_050: correct encoded cube returned after default clockwise rotation
#   test_051: correct encoded cube returned after multiple face rotations in both directions
#   test_052: correct encoded cube returned after single non-default clockwise rotation
#   test_053: correct encoded cube returned after single non-default counterclockwise rotation
        
    def test_010_ShouldInstantiateCube(self):
        parm = {'op':'info',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}        
        test_cube = Cube(parm)
        self.assertIsInstance(test_cube, Cube, "Not an instance of Cube")
    
    def test_020_ShouldPopulateCubeState(self):
        parm = {'op':'info',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'} 
        test_cube = Cube(parm)
        expectedResult = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = test_cube.cube_state
        self.assertEqual(expectedResult, actualResult, "error: cube state property not set") 
    
    def test_030_ShouldReturnCubeString(self):
        parm = {'op':'info',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'} 
        test_cube = Cube(parm)
        expectedResult = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = test_cube.getCube()
        self.assertEqual(expectedResult, actualResult, "error: cube get failed")
    
    def test_040_ShouldReturnValidCubeStatus(self):
        parm = {'op':'info',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'} 
        test_cube = Cube(parm)
        actualResult = test_cube._isValidCube()
        self.assertTrue(actualResult)
        
    def test_050_ShouldReturnCorrectEncodingAfterDefaultRotation(self):
        parm = {'op':'solve',
                'rotate': 'F',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        test_cube = Cube(parm)
        actualResult = test_cube._rotate()
        expectedResult = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        self.assertEquals(expectedResult, actualResult,"incorrect rotation result")
    
    def test_051_ShouldReturnCorrectEncodingAfterMultipleRotations(self):
        parm = {'op':'solve',
                'rotate': 'FfR',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        test_cube = Cube(parm)
        actualResult = test_cube._rotate()
        expectedResult = 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb'
        self.assertEquals(expectedResult, actualResult,"incorrect rotation result")
    
    def test_052_ShouldReturnCorrectEncodingAfterSingleClockwiseRotation(self):
        parm = {'op':'solve',
                'rotate': 'L',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        test_cube = Cube(parm)
        actualResult = test_cube._rotate()
        expectedResult = 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy'
        self.assertEquals(expectedResult, actualResult,"incorrect rotation result")


   
  
# Sad path tests
#    test_910: error on missing constructor argument to Cube()
#    test_920: error on missing encoded cube string key

    def test_910_ShouldErrorOnMissingConstructorArgument(self):
        expectedResult = '<class \'TypeError\'>'
        try:
            test_cube = Cube()
            actualResult = str(type(test_cube.getCube()))
        except Exception as e:
            actualResult = str(type(e))
        self.assertEquals(expectedResult, actualResult, 'invalid cube constructor')
    
    def test_920_ShouldErrorOnMissingEncodedCubeStringArgument(self):
        parm = {'op':'info'}
        expectedResult = '<class \'AttributeError\'>'
        try:
            test_cube = Cube(parm)
            actualResult = test_cube.getCube()
        except AttributeError as e:
            actualResult = str(type(e))
        self.assertEquals(expectedResult, actualResult, 'invalid cube constructor')
                                                            
        
           

