def kangaroo(x1, v1, x2, v2):
    '''
    It should return YES if they reach the same position at the same time, 
    or NO if they don't.

    kangaroo has the following parameter(s):
    x1, v1: integers, starting position and jump distance for kangaroo 1
    x2, v2: integers, starting position and jump distance for kangaroo 2
    '''
    if ( ( x1 < x2 ) and (v1 < v2) ) or ( ( x2 < x1 ) and ( v2 < v1 ) ):
        return "NO"
    elif ( x1 == x2 ) and ( v1 != v2 ):
        return "NO"
    elif (v1 == v2) and (x1 != x2):
        return "NO"
    else:
        final_x = ( (v2)*(x1) - (v1)*(x2) ) / (v2 - v1)
        N = (final_x - x1) % v1
        
        if N == 0:
            return "YES"
        else:
            return "NO"