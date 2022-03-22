'''
    Created on ?
    @author: Brian Adair
    
'''

# Brian Adair 
# COMP 6700 - Assignment 02
# 2022-01-31 


CUBE_STR_LENGTH = 54
COLOR_CHOICES = 6
COLOR_OCCURRENCES = 9

sides_dict = {1: 3, 2: 4, 5: 6}
tuple_arr = [(1,)]
side_tuple_arr = [(1,30,43),(2,44),(3,10,45),(4,33),(6,13),(7,36,46),(8,47),
             (9,16,48),(11,42),(12,19,39),(15,22),(17,51),(18,25,54),
             (20,38),(21,28,37),(24,31),(26,53),(27,34,52),(29,40),(35,49)]
middle_tuple_arr = [(5,23),(14,32),(41,50)]

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)  
         
    if(encodedCube == None):
        result['status'] = 'error: no key for cube exists'
        
    elif(type(encodedCube) is not str):
        result['status'] = 'error: value for cube should be of type str'
        
    elif(len(encodedCube) > CUBE_STR_LENGTH):
        result['status'] = 'error: cube str length exceeds 54 chars'
        
    elif(len(encodedCube) < CUBE_STR_LENGTH):
        result['status'] = 'error: cube str length is less than 54 chars'
        
    elif(not encodedCube.isalnum()):
        result['status'] = 'error: cube str contains invalid color choice characters'
        
    elif(len(set(encodedCube)) > COLOR_CHOICES):
        result['status'] = 'error: too many colors'
        
    elif(len(set(encodedCube)) < COLOR_CHOICES):
        result['status'] = 'error: not enough unique colors'
        
    elif(not _check_color_occurrences(encodedCube)):
        result['status'] = 'error: some color has too few occurrences on the cube'
    
    elif(_check_opposite_side_match(encodedCube, 1, 3)):
        result['status'] = 'error: middle colors on sides S1 and S3 cannot match'
        
    elif(_check_opposite_side_match(encodedCube, 2, 4)):
        result['status'] = 'error: middle colors on sides S2 and S4 cannot match'
        
    elif(_check_opposite_side_match(encodedCube, 5, 6)):
        result['status'] = 'error: middle colors on sides S5 and S6 cannot match'
    
    elif(_check_nonunique_middle_colors(encodedCube)):
        result['status'] = 'error: each middle color must be unique'
        
    #elif(_check_adjacency_mismatch(encodedCube)):
    #    result['status'] = 'error: adjacency mismatch of colors'
    else:
        result['status'] = 'ok'
        
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

    if side_a == side_b:
        return True  
        
    return False  


def _check_nonunique_middle_colors(cube):
    start = 0
    mid = 4
    color_set = []
    
    for i in range(0,COLOR_CHOICES):
        start = i * COLOR_OCCURRENCES
        mid_color = start + mid
        color_set.append(cube[mid_color])
        
    if (len(set(color_set)) < COLOR_CHOICES):
        return True
    else:
        return False


def _check_adjacency_mismatch(cube):

    flag = True

    for pair in middle_tuple_arr:
        mid_a = pair[0]
        mid_b = pair[1]
        #mid_a_color = cube[mid_a -1]
        #mid_b_color = cube[mid_b -1]

    for m in pair:
        if (m == mid_a):
            opposite = mid_b
        else:
            opposite = mid_a
      
        for i in range(m - 4, m+5):
            if cube[i-1] != cube[m-1]:
                pass
            else:
                for sides in side_tuple_arr:
                    if i in sides:
                        for position in sides:
                            if position == i:
                                pass
                            else:
                                if cube[position-1] == cube[opposite-1]:
                                    flag = False
    return flag
                
            


