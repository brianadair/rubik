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
#                    with a value of 'ok' when all conditions for a valid cube are met, 
#                    or an error message indicating the failed condition of the cube's properties. 
#
#        confidence level: BVA
#
# Happy path
#    test 010: verify a solved cube
#    test 020: key for cube exists in the dictionary input parameter
#    test 030: value for cube is a string
#    test 040: value for cube contains 54 elements
#    test 050: cube value contains 9 occurrences of 6 colors
#    test 060: every middle face has a different color per side
#    
# Sad path
#    test 910:
#
#
#

    # Boundary Value Analysis Tests
    # test 010
    
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

