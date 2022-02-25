import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):

# Happy Path tests
#    - test_010: cube validated before operations performed
#    - test_020: 
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
        
