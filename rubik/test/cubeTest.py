# Brian Adair 
# COMP 6700 - Assignment 03
# 2022-02-24

# Tests of cube properties and methods

import rubik.cube as cube
import unittest
from rubik.cube import Cube


class Test(unittest.TestCase):

# Happy path tests
    # create a model
    # populate a model
    # get a model
    # rotate
    
    def test_010_ShouldInstantiateCube(self):
        parm = {'op':'info',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}        
        test_cube = cube.Cube(parm)
        self.assertIsInstance(test_cube, Cube, "Not an instance of Cube")
    
    def test_020_ShouldPopulateCubeState(self):
        parm = {'op':'info',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'} 
        test_cube = cube.Cube(parm)
        expectedResult = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = test_cube.cube_state
        self.assertEqual(expectedResult, actualResult, "error: cube state property not set") 
     
    def testName(self):
        pass
