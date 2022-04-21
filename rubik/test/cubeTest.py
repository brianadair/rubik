'''
    Created on ?
    @author: Brian Adair
    
'''
# Brian Adair 
# COMP 6700 - Assignment 05
# 2022-02-24

# Tests of cube properties and methods

import unittest
from rubik.cube import Cube
from pickle import TRUE

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

    def test_053_ShouldReturnCorrectEncodingAfterSingleCounterClockwiseRotation(self):
        parm = {'op':'solve',
                'rotate': 'd',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        test_cube = Cube(parm)
        actualResult = test_cube._rotate()
        expectedResult = 'ggggggrrrrrrrrrbbbbbbbbbooooooooogggwwwwwwwwwyyyyyyyyy'
        self.assertEquals(expectedResult, actualResult,"incorrect rotation result")
    
    #@unittest.skip("Fixing error in top flip")    
    def test_060_ShouldReturnTopDaisySolutionSequence(self):
        parm = {'op': 'solve',
        #        'cube': 'ybbbbwggboywrrbygwrgoygyroggobrorryowwbwygowwyrrowoybg'}
        #        'cube': 'wwwggggggbwwrrrrrrybbybbybboogooyooyyygyygrrrooowwbwwb'}
        #         'cube': 'bgwggwrwwgrrrrbbbbyryybryyrowwbooyogggggyyryowoobwwboo'}
        #        'cube': 'ygyrgogywrbwyrggrwobywborwogogwobbyorybgyoorbwgrrwwybb'}
                'cube': 'bbwggryowggbwrorwwybogbygyyyboooygwgbyrryrwoorwbbwgorr'}
        test_cube = Cube(parm)
        result = test_cube._solveTopDaisySolution()
        cube = test_cube.getCube()
        actualResult = test_cube._isTopDaisy()
        #print(f"Cube: bbwggryowggbwrorwwybogbygyyyboooygwgbyrryrwoorwbbwgorr")
        #print(f"Solution: {result}")
        #print(f"Cube after top daisy solution: {cube}")
        expectedResult = True
        self.assertEquals(expectedResult, actualResult,"incorrect solution result")
    
    def test_061_ShouldFlipUpperEdgesPhaseOne(self):
        parm = {'op': 'solve',
                #'cube': 'wwwggggggbwwrrrrrrybbybbybboogooyooyyygyygrrrooowwbwwb'} #fUlfUl
                'cube': 'ggbggbbbrwwworgwrgybyobyrowrroroyrgobwgwyoywoyygrwbbyo'}  #rUf
        test_cube = Cube(parm)
        result = test_cube._flipTopLayerEdges()
        #expectedResult = 'gwwwggwggybborrorroorybrybbgrrgoowoooyywyywggbyybwbrwb'
        expectedResult = 'rUf'
        self.assertEquals(result, expectedResult)
        
    def test_062_ShouldReturnTrueOnTopEdgeToBeFlipped(self):
        parm = {'op': 'solve',
                'cube': 'wwwggggggbwwrrrrrrybbybbybboogooyooyyygyygrrrooowwbwwb'}
        test_cube = Cube(parm)
        actualResult = test_cube._isFlippedTopEdgePhaseOne()
        expectedResult = True
        self.assertEquals(actualResult, expectedResult) 
        
    def test_063_ShouldReturnTrueOnBottomEdgeToBeFlipped(self):
        parm = {'op': 'solve',
                'cube': 'rbbbggrwwooryrrbrrgroyboybyggwgoowgwywowyygyyboorwbgwb'} 
        test_cube = Cube(parm)
        actualResult = test_cube._isFlippedBottomEdgePhaseOne()
        expectedResult = True
        self.assertEquals(actualResult, expectedResult)
    
    def test_064_ShouldRotateMiddleEdgesToTopPhaseOne(self):
        parm = {'op': 'solve',
                #'cube': 'gwwwggwggybborrorroorybrybbgrrgoowoooyywyywggbyybwbrwb'}
                #'cube': 'grrbgwbwwyrrrrgbbbgggobywyyygwoooobyowwyygoygroorwwbbr'}
                'cube': 'ygyrgogywrbwyrggrwobywborwogogwobbyorybgyoorbwgrrwwybb'}
        test_cube = Cube(parm)
        actualResult = test_cube._daisyMiddleLayer()
        cube = test_cube.getCube()
        #print(actualResult)
        #print('rbbbggrwwooryrrbrrgroyboybyggwgoowgwywowyygyyboorwbgwb')
        #print(cube)
        #expectedResult = "RuR"
        expectedResult = 'ruruubuuL'
        self.assertEquals(actualResult, expectedResult)      
    
    #@unittest.skip("Fixing bottom code")
    def test_065_ShouldRotateBottomEdgesToTopPhaseOne(self):
        parm = {'op': 'solve',
                'cube': 'rbbbggrwwooryrrbrrgroyboybyggwgoowgwywowyygyyboorwbgwb'}
        test_cube = Cube(parm)
        actualResult = test_cube._daisyBottomLayer()
        cube = test_cube.getCube()
        #print(actualResult)
        #print('rbbbggrwwooryrrbrrgroyboybyggwgoowgwywowyygyyboorwbgwb')
        #print(cube)
        #expectedResult = "FFuBB"
        expectedResult = 'FFfUluuBB'
        self.assertEquals(actualResult, expectedResult)

    @unittest.skip("Using another test for bottom layer")
    def test_066_ShouldRotateFacesToDownCrossAfterDaisy(self):
        parm = {'op': 'solve',
                #'cube': 'wbwogoogroooyrrgoywrrgbygbgbgrrobrryywgwywbwbbyybwgwyo'}
                #'cube': 'orrrgybbrwgogrogywgbggbrooowowyogbbyrwywywbwbrryywoybg'
                'cube': 'ygrggoooywrwyrbbryrbrrbygywyooroybowgwgwywbwbggrbwgobo'}
        test_cube = Cube(parm)
        actualResult = test_cube._solveDownCrossSolution()
        #expectedResult = 'UUUFFUURRUBBLL'  #cube1
        expectedResult = 'UFFUURRUBBLL'  #cube2
        self.assertEquals(actualResult, expectedResult)                        

    def test_090_ShouldReturnTrueOnBottomCross(self):
        parm = {'op': 'solve',
                #'cube': 'yoroggogrbgrrrrgrogbrybowbywroyobgowbywbyybgygwywwwowb' #cube1
                'cube': 'yogggrogryrbbrrwrywyryborbywooyoybowbbobygbgogwgwwwrwg'}
        test_cube = Cube(parm)
        actualResult = test_cube._isBottomCross() #cube1
        expectedResult = True
        self.assertEquals(actualResult, expectedResult)
    
    def test_091_ShouldReturnTrueOnBottomComplete(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1
                'cube': 'bgobbybbbyrgorbrrryryygrgggogygooooobbryyyrogwwwwwwwww'}
        test_cube = Cube(parm)
        actualResult = test_cube._isBottomComplete()
        expectedResult = True
        self.assertEquals(actualResult, expectedResult)
        
    def test_0911_ShouldReturnTrueOnMiddleLayerComplete(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'bgobbybbbyrgorbrrryryygrgggogygooooobbryyyrogwwwwwwwww'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._isMiddleLayerComplete()
        expectedResult = True
        self.assertEquals(actualResult, expectedResult)

    def test_0912_ShouldReturnFalseOnMiddleLayerComplete(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'bgobbybbbyrgorbrrryryygrgggogygooooobbryyyrogwwwwwwwww'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._isMiddleLayerComplete()
        expectedResult = False
        self.assertEquals(actualResult, expectedResult)
        
    def test_0913_ShouldReturnTrueOnSolvedCube(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'bgobbybbbyrgorbrrryryygrgggogygooooobbryyyrogwwwwwwwww'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._isCubeSolved()
        expectedResult = True
        self.assertEquals(actualResult, expectedResult) 

    def test_0914_ShouldReturnFalseOnUnsolvedCube(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'bgobbybbbyrgorbrrryryygrgggogygooooobbryyyrogwwwwwwwww'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._isCubeSolved()
        expectedResult = False
        self.assertEquals(actualResult, expectedResult) 
        
    def test_0915_ShouldReturnTrueOnSideVerticalLineColorMatch(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
                'cube': 'wgbbggogbryrororryyrrybyobbggoroooogwbgyybgrwywywwwwwb'}
        test_cube = Cube(parm)
        actualResult = test_cube._isSideFaceMiddleVerticalMatched(0)
        expectedResult = True
        self.assertEquals(actualResult, expectedResult)
   
    def test_0916_ShouldReturnFalseOnSideVerticalLineColorMatch(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._isSideFaceMiddleVerticalMatched(1)
        expectedResult = False
        self.assertEquals(actualResult, expectedResult)    
       
    @unittest.skip("Work in progress")    
    def test_092_ShouldMoveIncorrectBottomCornersToTopLayer(self):
        parm = {'op': 'solve',
                'cube': 'yyrrggwgrwbborygrwooorbygbwgbbgogoooybyyyrrobbwywwwgwr'
                }
        test_cube = Cube(parm)
        solution = test_cube._flipIncorrectBottomCornersToTop()
        cube = test_cube.cube_state
        expectedResult = test_cube._isBottomCornerPlacementCorrect()
        self.assertEquals(solution, expectedResult)     
        
    def test_093_ShouldReturnTrueOnCorrectBottomCorners(self):
        parm = {'op': 'solve',
                #'cube': 'yyrrggwgrwbborygrwooorbygbwgbbgogoooybyyyrrobbwywwwgwr'
                #'cube':'rbrgggwgrbooorbbrrgbyrbrwbbbrggoyoogooyyyyyyyowwwwwwwg'
                'cube':'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'
                }
        test_cube = Cube(parm)
        actualResult = test_cube._isBottomCornerPlacementCorrect()
        check = test_cube._isBottomCross()  #did we maintain the solution from stage 2
        expectedResult = True
        self.assertEquals(actualResult, expectedResult) 
        self.assertEquals(check, expectedResult)
    
    def test_094_ShouldReturnSolutionToMoveBottomCornerIncorrectPlacements(self):
        parm = {'op': 'solve',
                #'cube': 'yyrrggwgrwbborygrwooorbygbwgbbgogoooybyyyrrobbwywwwgwr'
                'cube':'ogyrgybgwgggbrobryoobybrobryyybogworrbwryogyrwwowwwgwb'
                }    
        test_cube = Cube(parm)
        #solution = test_cube._OLDmoveBottomCornerIncorrectPlacements()
        solution = test_cube._moveBottomCornerIncorrectPlacements()
        expectedResult = 'luLfuFfuFbuB'
        self.assertEquals(solution, expectedResult)
    
    @unittest.skip("in progess, last phase") 
    def test_095_ShouldReturnSolutionToMoveCornerToCorrectSideAdjacency(self):
        parm = {'op': 'solve',
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'} 
        test_cube = Cube(parm)
        actualResult = test_cube._moveTopCornersToCorrectColorAdj()
        actualResult = test_cube._moveTopCornersToCorrectColorAdj()

        expectedResult = 'UUFufUufUFUurURUubUB'
        self.assertEquals(actualResult, expectedResult)
    
    def test_096_ShouldReturnEmptyRotationStringOnBottomLayerCornerWithNoMatch(self):
        parm = {'op': 'solve',
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'} #cube1
                #'cube': 'yogggrogryrbbrrwrywyryborbywooyoybowbbobygbgogwgwwwrwg'}       
        test_cube = Cube(parm)
        adjList = [36,27,20]
        midColors = ['b','o','w']
        actualResult = test_cube._getTopRotationForBottomLayerPositionMatch(adjList, midColors)
        expectedResult = ''
        self.assertEquals(actualResult, expectedResult)
        
    def test_097_ShouldReturnRotationStringOnBottomLayerCornerAfterMatchedPosition(self):
        parm = {'op': 'solve',
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'} #cube1
                #'cube': 'yogggrogryrbbrrwrywyryborbywooyoybowbbobygbgogwgwwwrwg'}       
        test_cube = Cube(parm)
        adjList = [0, 29, 42]
        midColors = ['g', 'o', 'w']
        actualResult = test_cube._getTopRotationForBottomLayerPositionMatch(adjList, midColors)
        expectedResult = 'U'
        self.assertEquals(actualResult, expectedResult)
        
    def test_098_ShouldReturnTrueOnTopCornerInCorrectColorMatchPositionForBottom(self):
        pass
    
    #@unittest.skip('part of solving middle layer')
    def test_09901_ShouldReturnSideFaceAdjColorListForFace(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._getSideFaceAdjacencyMiddleColors(0)
        expectedResult = ['o','r']
        self.assertEquals(actualResult, expectedResult)
        
    def test_09902_ShouldReturnAllSideFaceAdjColorPairings(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._getSideFaceColorPairings()
        print(f"Color pairings in test: {actualResult}")
    
    def test_09903_ShouldReturnTrueOnMismatchedRightEdgeForMiddleLayer(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
                'cube':'bgoggboggggbororryryrybyobbyrrroooowgbwbyrywygywwwwwwb'} #cube above after FF move
        test_cube = Cube(parm)
        actualResult = test_cube._isRightEdgeMismatchedForMiddleLayer(0,[5,12])
        print(f"9903 Edge mismatch?: {actualResult}")
        self.assertEquals(actualResult, True)

    def test_09904_ShouldReturnTrueOnMatchedRightEdgeForMiddleLayer(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
                'cube': 'bgoyggrgbwgbororryryoybbobggoooorrryybwwyrwyggwybwwwwb'} #above cube after ll move
        test_cube = Cube(parm)
        actualResult = test_cube._isRightEdgePlacementCorrectForFace(2)
        print(f"9904 Right edge of face matched?: {actualResult}")
        self.assertEquals(actualResult, True)
        
    def test_09905_ShouldReturnSolutionStringForMiddleLayerRightRotation(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
                #'cube': 'bgoyggrgbwgbororryryoybbobggoooorrryybwwyrwyggwybwwwwb'} #above cube after ll move
        test_cube = Cube(parm)
        actualResult = test_cube._rotateRightForMiddleLayer(0, 1)
        print(f"9905 sequence: {actualResult}")
        print(f"9905 cube: {test_cube.cube_state}")
        self.assertEquals(actualResult, 'URurufUF')

    def test_09906_ShouldReturnSolutionStringForMiddleLayerLeftRotation(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
                #'cube': 'bgoyggrgbwgbororryryoybbobggoooorrryybwwyrwyggwybwwwwb'} #above cube after ll move
        test_cube = Cube(parm)
        actualResult = test_cube._rotateLeftForMiddleLayer(0, 3)
        print(f"9906 sequence: {actualResult}")
        print(f"9906 cube: {test_cube.cube_state}")
        self.assertEquals(actualResult, 'ulULUFuf')
    
    def test_09907_ShouldReturnRightTargetForMiddleLayerFinalMove(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
                'cube': 'wgbbggogbryrororryyrrybyobbggoroooogwbgyybgrwywywwwwwb'} #above cube after U move
        test_cube = Cube(parm)
        actualResult = test_cube._getTargetForMiddleLayerFinalSequence(0)
        print(f"9907 target: {actualResult}")
        self.assertEquals(actualResult, 1)
    
    @unittest.skip('no good test example yet')    
    def test_09908_ShouldReturnLeftTargetForMiddleLayerFinalMove(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
                'cube': 'ogbggggboygbwroyryryrybyobbyrgroyoowgbwbyrworrogwwwwwb'} #above cube after f move
        test_cube = Cube(parm)
        actualResult = test_cube._getTargetForMiddleLayerFinalSequence(0)
        print(f"9908 target: {actualResult}")
        self.assertEquals(actualResult, 1)

    def test_09909_ShouldReturnSolutionToMoveTopEdgeToMiddleLayerForFace(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                'cube': 'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'}#cube2 false
        test_cube = Cube(parm)
        actualResult = test_cube._positionTopEdgeToMiddleLayer(0)
        expectedResult = 'UURurufUF'
        print(f"9909 solution: {actualResult}")
        self.assertEquals(actualResult, expectedResult)
    
    def test_09910_ShouldReturnSolutionToMiddleLayer(self):
        parm = {'op': 'solve',
                #'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'} #cube1 true
                #'cube': 'rbyrbbgbbboorrrrrrbgwggggggbbyooyooooyyoyygyrywwwwwwww'}#cube2 false
                'cube':'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb}'
        test_cube = Cube(parm)
        actualResult = test_cube._solveMiddleLayerSolution()
        expectedResult = ''
        print(f"9910 solution: {actualResult}")
        self.assertEquals(actualResult, expectedResult)

    def test_101_ShouldReturnTopMiddleColor(self):
        parm = {'op': 'solve',
                'cube': 'ybbbbwggboywrrbygwrgoygyroggobrorryowwbwygowwyrrowoybg'}
        test_cube = Cube(parm)
        actualResult = test_cube._getTopDaisyMiddle()
        expectedResult = 'y'
        self.assertEquals(expectedResult, actualResult)
     
    @unittest.skip("Only for trying ideas")    
    def test_102_YellowTestIdea(self):
        parm = {'op': 'solve',
                #'cube': 'yyrrggwgrwbborygrwooorbygbwgbbgogoooybyyyrrobbwywwwgwr'
                'cube': 'bryygbgggbyyoryrrrgryobybbboorrogooogbrgybygowwwwwwwww' #cube with bottom layer complete
                }
        test_cube = Cube(parm)
        actualResult = test_cube._tryNeuralFive()
        #actualResult = test_cube._isBottomCross()
        if test_cube._isMiddleLayerComplete():
            print(f"Solved middle layer: {test_cube.getCube()} ({actualResult})")
        expectedResult = True
        self.assertEquals(expectedResult, actualResult)

    def test_103_ShouldCreateRandomScrambledCubeFromSolved(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
                }
        test_cube = Cube(parm)
        cube = test_cube._getRandomScramble()
        actualResult = test_cube._isValidCube()
        expectedResult = True
        self.assertEquals(actualResult, expectedResult)
        self.assertNotEquals(cube, 'gggggggggrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww')

    @unittest.skip("only use for randomized testing when done")
    def test_104_ShouldCreateTopDaisyOnManyRandomGeneratedCubes(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
                }
        test_cube = Cube(parm)
        for r in range(1,500):
            test_cube._getRandomScramble()
            result = test_cube._isValidCube()
            print(f"Test Cube {r}: {test_cube.getCube()} initialized")
            self.assertEquals(result, True)
            test_cube._solveTopDaisySolution()
            result = test_cube._isTopDaisy()
            print(f"Test Cube {r}: {result} {test_cube.getCube()}")
            self.assertEquals(result, True)
            
    @unittest.skip("only use for randomized testing when done")
    def test_105_ShouldCreateBottomCrossOnManyRandomGeneratedCubes(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
                }
        test_cube = Cube(parm)
        for r in range(1,500):
            test_cube._getRandomScramble()
            result = test_cube._isValidCube()
            #print(f"Test Cube {r}: {test_cube.getCube()} initialized")
            self.assertEquals(result, True)
            solution = test_cube._solveTopDaisySolution()
            print(f"Daisy result: {test_cube._isTopDaisy()}")
            solution = solution + test_cube._solveDownCrossSolution()
            result = test_cube._isBottomCross()
            #print(f"Test Cube {r}: {result} {test_cube.getCube()} {solution}")
            self.assertEquals(result, True)
            
    @unittest.skip("only use for randomized testing when done")
    def test_106_ShouldCreateBottomCompleteOnManyRandomGeneratedCubes(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
                }
        test_cube = Cube(parm)
        resultTrue = 0
        resultFalse = 0
        middleTrue = 0
        middleFalse = 0
        for r in range(1,500):
            test_cube._getRandomScramble()
            result = test_cube._isValidCube()
            #print(f"Test Cube {r}: {test_cube.getCube()} initialized")
            self.assertEquals(result, True)
            solution = test_cube._solveTopDaisySolution()
            result = test_cube._isTopDaisy()
            self.assertEquals(result, True)
            solution = solution + test_cube._solveDownCrossSolution()
            
            result = test_cube._isBottomCross()
            self.assertEquals(result, True)
            solution = solution + test_cube._solveBottomLayerSolution()
            result = test_cube._isBottomComplete()
            if result == True:
                resultTrue = resultTrue + 1
            else:
                resultFalse = resultFalse + 1
            #print(f"Test Cube {r}: {result} {test_cube.getCube()} {solution}")
            
            if test_cube._isBottomComplete():
                solution = solution + test_cube._solveMiddleLayerSolution()
                result = test_cube._isMiddleLayerComplete()
                if result == True:
                    middleTrue = middleTrue + 1
                else:
                    middleFalse = middleFalse + 1            
            
            #self.assertEquals(result, True)
        print(f"Final bottom results: True ({resultTrue}) False ({resultFalse})")
        print(f"Final middle results: True ({middleTrue}) False ({middleFalse})")
       
    def test_107_ShouldSolveBottomLayerOnDownCrossEncodedCube(self):
        parm = {'op': 'solve',
                #'cube': 'yyrrggwgrwbborygrwooorbygbwgbbgogoooybyyyrrobbwywwwgwr'
                #'cube':'rbrgggwgrbooorbbrrgbyrbrwbbbrggoyoogooyyyyyyyowwwwwwwg'
                'cube':'ggobggogbwgbororryryrybyobbyrrrooooggbwbyrwygywywwwwwb'
                }
        test_cube = Cube(parm)
        actualResult = test_cube._solveBottomLayerSolution()
        check = test_cube._isBottomComplete()  #did we maintain the solution from stage 2
        print(f"Test 107: cube {test_cube.cube_state}")
        expectedResult = True
        #self.assertEquals(actualResult, expectedResult) 
        self.assertEquals(check, expectedResult) 
  
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
        parm = {'op':'solve'}
        expectedResult = '<class \'AttributeError\'>'
        try:
            test_cube = Cube(parm)
            actualResult = test_cube.getCube()
        except AttributeError as e:
            actualResult = str(type(e))
        self.assertEquals(expectedResult, actualResult, 'invalid cube constructor')
        
    def test_930_ShouldReturnFalseOnUnknownRotateCommandCode(self):
        parm = {'op': 'solve',
                'rotate': 'Z',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        expectedResult = False
        test_cube = Cube(parm)
        actualResult = test_cube._isRotationValid()
        self.assertEquals(expectedResult, actualResult)
        
    def test_940_ShouldReturnFalseOnCorrectBottomCorners(self):
        parm = {'op': 'solve',
                #'cube': 'yyrrggwgrwbborygrwooorbygbwgbbgogoooybyyyrrobbwywwwgwr'
                'cube':'ogyrgybgwgggbrobryoobybrobryyybogworrbwryogyrwwowwwgwb'
                }
        test_cube = Cube(parm)
        actualResult = test_cube._isBottomCornerPlacementCorrect()
        expectedResult = False
        self.assertEquals(actualResult, expectedResult)  
        
    #@unittest.skip("only use for randomized testing when done")
    #test can fail if random cube is generated with a bottom cross
    def test_999_ShouldFalseOnRandomizedBottomCrossAttemptWithNonDaisyCubeState(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
                }
        test_cube = Cube(parm)
        for r in range(1,500):
            solution = ''
            test_cube._getRandomScramble()
            result = test_cube._isValidCube()
            #print(f"Test Cube {r}: {test_cube.getCube()} initialized")
            self.assertEquals(result, True)
            #solution = test_cube._solveTopDaisySolution()
            #print(f"Daisy result: {test_cube._isTopDaisy()}")
            solution = solution + test_cube._solveDownCrossSolution()
            result = test_cube._isBottomCross()
            #print(f"Test Cube {r}: {result} {test_cube.getCube()} {solution}")
            self.assertEquals(result, False)
            
                                                            
        
           

