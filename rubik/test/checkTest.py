# Brian Adair 
# COMP 6700 - Assignment 02
# 2022-01-31 

from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
    
# Analysis
#    check(parms):
#        inputs:
#            parms: dictionary, mandatory, validated
#                    key: 'op', string, mandatory, validated
#                    key: 'cube', string, mandatory, unvalidated
#
#        outputs:
#            side-effects: no state change
#            returns: dictionary, contains one key ('status') 
#                     with a value of 'ok' when all conditions for a valid cube are met, 
#                     or an error message indicating the failed condition of the cube's 
#                     properties. 
#
#        confidence level: BVA
#
# Happy path definitions: all successful test results will return {'status','ok'}
#    test 010: verify a solved cube
#    test 020: key for cube exists in the dictionary input parameter
#    test 030: value for cube is a string
#    test 040: BVA test, value for cube contains 54 elements
#    test 050: BVA test cube value contains 9 occurrences of 6 colors
#    test 060: every middle face has a different color per side
#    test 070: EC: adjacent colors are not also on the opposite middle
  
# Sad path definitions
#    test 910: no property for cube in dictionary parameter
#    test 911: non-string value for cube: {'cube', False}
#    test 920: greater than high bound of elements (+1) {'cube','bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'}
#    test 921: less than low bound of elements (-1) {'cube','bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'}
#    test 922: non-alphanumeric characters for color choice
#    test 930: greater than high bound of unique colors: 7
#    test 931: less than low bound of unique colors: 5
#    test 940: less than low bound of unique color occurrences: 8
#    test 950: Opposite sides S1 and S3 share the same color in the middle position
#    test 951: Opposite sides S2 and S4 share the same color in the middle position
#    test 952: Opposite sides S5 and S6 share the same color in the middle position
#    test 960: EC: adjacent colors that share middle color from opposite side of facing side's middle
    
# Happy Path Tests
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_020_ShouldReturnOkWithCubeKeySet(self):
        parm = {'op':'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_030_ShouldReturnOkWithCubeValueAsString(self):
        parm = {'op':'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_040_ShouldReturnOkExactStringLength(self):
        parm = {'op':'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_050_ShouldReturnOkWithCorrectColorCounts(self):
        parm = {'op':'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_060_ShouldReturnOkWithCorrectMiddleColorValues(self):
        parm = {'op':'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

    def test_check_070_ShouldReturnOkWithCorrectColorAdjacencies(self):
        parm = {'op':'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
# Sad Path Tests
    def test_check_910_ShouldTestCubePropertyDoesNotExist(self):
        parm = {'op': 'check'}
        expected_result = 'error: no key for cube exists'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)
        
    def test_check_911_ShouldTestNonStringValueForCube(self):
        parm = {'op': 'check', 'cube': False}
        expected_result = "error: value for cube should be of type str"
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)
    
    def test_check_920_ShouldTestHigherThanExactLengthBound(self):
        parm = {'op': 'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWgg'}
        expected_result = 'error: cube str length exceeds 54 chars'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)
    
    def test_check_921_ShouldTestLowerThanExactLengthBound(self):
        parm = {'op': 'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWW'}
        expected_result = 'error: cube str length is less than 54 chars'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)

    def test_check_922_ShouldTestNonAlphaNumericCharacters(self):
        parm = {'op': 'check',
                'cube':'44-44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        expected_result = 'error: cube str contains invalid color choice characters'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)
        
    def test_check_930_ShouldTestUniqueColorUpperBound(self):
        parm = {'op': 'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggDAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        expected_result = 'error: too many colors'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)

    def test_check_931_ShouldTestUniqueColorLowerBound(self):
        parm = {'op': 'check',
                'cube':'44W44W44WFFFFFFFFFyggyggyggFFFFFFFFFyy4yy4yy4WWgWWgWWg'}
        expected_result = 'error: not enough unique colors'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)
    

    def test_check_940_ShouldTestLowerThanUniqueColorOccurrencesBound(self):
        parm = {'op': 'check',
                'cube':'44W44W44WrWrrrrrrryggyggyggAAAAAAAAAyy4yy4yy4WWgWWgWWg'}
        expected_result = 'error: some color has too few occurrences on the cube'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)
        
    def test_check_950_ShouldTestSharedMiddleColorsOnOppositeSidesS1S3(self):
        parm = {'op': 'check',
                'cube':'44W44W44Wrrrrrrrrryggy4gyggAAAAAAAAAyygyy4yy4WWgWWgWWg'}
        expected_result = 'error: middle colors on sides S1 and S3 cannot match'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)   
 
    def test_check_951_ShouldTestSharedMiddleColorsOnOppositeSidesS2S4(self):
        parm = {'op': 'check',
                'cube':'44W44W44WrrrrArrrryggyggyggAArAAAAAAyy4yy4yy4WWgWWgWWg'}
        expected_result = 'error: middle colors on sides S2 and S4 cannot match'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)   
        
    def test_check_952_ShouldTestSharedMiddleColorsOnOppositeSidesS5S6(self):
        parm = {'op': 'check',
                'cube':'44W44W44WrrrrrrrrryggyggyggAAAAAAAAAyy4yy4Wy4WWgWygWWg'}
        expected_result = 'error: middle colors on sides S5 and S6 cannot match'
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, expected_result)    
    

    # def test_check_960_EC_ShouldTestIncorrectColorAdjacencyLocations(self):
    #     parm = {'op': 'check'}
    #     expected_result = 'error: color adjacency rules not met'
    #     result = check._check(parm)
    #     self.assertIn('status', result)
    #     status = result.get('status', None)
    #     self.assertEqual(status, expected_result) 

