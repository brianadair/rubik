#import rubik.cube as rubik
#from pickle import FALSE

CUBE_STR_LENGTH = 54
COLOR_CHOICES = 6
COLOR_OCCURRENCES = 9

sides_dict = {1: 3, 2: 4, 5: 6}
msg = ""


def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)  
         
    if(encodedCube == None):
        result['status'] = 'error: no key for cube exists'
        print("No key for cube")
        
    elif(type(encodedCube) is not str):
        result['status'] = 'error: value for cube should be of type str'
        stat = _check_color_occurrences(encodedCube)
        print(type(encodedCube))
        print(stat)
        
    elif(len(encodedCube) > CUBE_STR_LENGTH):
        result['status'] = 'error: cube str length exceeds 54 chars'
        print(f"length is {len(encodedCube)}")
        
    elif(len(encodedCube) < CUBE_STR_LENGTH):
        result['status'] = 'error: cube str length is less than 54 chars'
        print(f"length is {len(encodedCube)}")
        
    elif(not encodedCube.isalnum()):
        result['status'] = 'error: cube str contains invalid color choice characters'
        print(encodedCube.isalnum())
        
    elif(len(set(encodedCube)) > COLOR_CHOICES):
        result['status'] = 'error: too many colors'
        print(set(encodedCube))
        
    elif(len(set(encodedCube)) < COLOR_CHOICES):
        result['status'] = 'error: not enough unique colors'
        print(set(encodedCube))
        
    elif(not _check_color_occurrences(encodedCube)):
        result['status'] = 'error: some color has too few occurrences on the cube'
        print("Not enough color occurrences")
    
    elif(_check_opposite_side_match(encodedCube, 1, 3)):
        result['status'] = 'error: middle colors on sides S1 and S3 cannot match'
        print("Sides S1 and S3 match")
        
    elif(_check_opposite_side_match(encodedCube, 2, 4)):
        result['status'] = 'error: middle colors on sides S2 and S4 cannot match'
        print("Sides S2 and S4 match")
        
    elif(_check_opposite_side_match(encodedCube, 5, 6)):
        result['status'] = 'error: middle colors on sides S5 and S6 cannot match'
        print("Sides S5 and S6 match")
        
    else:
        result['status'] = 'ok'
        print(parms)
        
    return result


def _check_color_occurrences(cube):
    
    flag = True
    if ((type(cube) is not str) or len(cube) != CUBE_STR_LENGTH):
        flag = False
        return flag

    color_dict = {}

    for i in cube:
        if i not in color_dict.keys():
            color_dict[i] = 1
        else:
            color_dict[i] += 1
    
    for key in color_dict.keys():
        if color_dict[key] < COLOR_OCCURRENCES:
            flag = False  
       
    return flag
    
def _check_opposite_side_match(cube, a, b):
    side_a = cube[a*9-5]
    side_b = cube[b*9-5]
    print(f"Side A {side_a}")
    print(f"Side B {side_b}") 
    if side_a == side_b:
        return True  
        
    return False  
    


