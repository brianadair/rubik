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
        expectedResult = ''
        self.assertEquals(expectedResult, actualResult,"incorrect rotation result")

