import numpy as np


def sameside(p1, p2, a, b):
    '''
        returns True if the points p1 and p2 lie on the same sides 
        of the edge ab and False otherwise

        p1, p2, a, b are all float tuples of length 2, or numpy array of shape (2, )
    '''
    # convert tuples into numpy array
    p1, p2, a, b = np.array(p1), np.array(p2), np.array(a), np.array(b) 

    cp1 = np.cross(b - a, p1 - a)
    cp2 = np.cross(b - a, p2 - a)
    if cp1 * cp2 >= 0:
        return True
    else:
        return False


def diffside(p1, p2, a, b):
    return not sameside(p1, p2, a, b)


def B_diff_side_A(triA, triB):
    ''' 
        all points of B are in different sides of certain edge A 
    '''
    a1, a2, a3 = triA
    b1, b2, b3 = triB

    # testing all edges of triangle A
    if diffside(a1, b1, a2, a3) and diffside(a1, b2, a2, a3) and diffside(a1, b3, a2, a3):
        return True
    if diffside(a2, b1, a3, a1) and diffside(a2, b2, a3, a1) and diffside(a2, b3, a3, a1):
        return True
    if diffside(a3, b1, a1, a2) and diffside(a3, b2, a1, a2) and diffside(a3, b3, a1, a2):
        return True
    return False


def intersect(triA, triB):
    if B_diff_side_A(triA, triB) or B_diff_side_A(triB, triA):
        return False
    else: 
        return True


if __name__ == '__main__':
    # generate two random triangles
    tri1 = np.random.rand(3, 2)
    tri2 = np.random.rand(3, 2)
        
    print(intersect(tri1, tri2))

