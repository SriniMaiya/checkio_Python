#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run find-sequence
from typing import List

def diag_el(r,c,matrix):                #https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
    diag = []; val=""
    for l in range(1, r+c):
        start_col = max(0, l-r)
        count = min(l, (c-start_col), r)
        for j in range(0, count):
            val += str(matrix[min(r, l)-j-1][start_col+j])
            if len(val)>=4:
                diag.append(val)
        val = ""
    return diag
    
    
def sums(lists):
    for x in lists:
        for i, y in enumerate(x):
            if i< len(x) - 3:
                if x[i:i+4].count(y) ==4:
                    return True
    return False
    
    
    
def checkio(matrix: List[List[int]]) -> bool:
    #replace this for solution
    r = len(matrix)
    c = len(matrix[0])
    rwise, cwise, diag1, diag2 = [],[],[],[]
    val = ""
    for j in range(c):
        for i in range(r):
            val += str(matrix[i][j])
        rwise.append(val)
        val = ""
        
    for i in range(r):
        for j in range(c):
            val += str(matrix[i][j])
        cwise.append(val)
        val = ""
    val = ""

    diag1 = diag_el(r,c,matrix=matrix)
    diag2 = diag_el(r,c, matrix= list(zip(*matrix[::-1])))
    print(sums(rwise), sums(cwise),sums(diag1), sums(diag2))
    return True if sums(rwise) or sums(cwise) or sums(diag1) or sums(diag2) else False
    
    
               
    
        
        
        
    
    
    return True or False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
    ]) == False
    
    assert checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True

    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    
    checkio([[2,7,6,2,1,5,2,8,4,4],
             [8,7,5,8,9,2,8,9,5,5],
             [5,7,7,7,4,1,1,2,6,8],
             [4,6,6,3,2,7,6,6,5,1],
             [2,6,6,9,8,5,5,6,7,7],
             [9,4,1,9,1,3,7,2,3,1],
             [5,1,4,3,6,5,9,3,4,1],
             [6,5,5,1,7,7,8,2,1,1],
             [9,5,7,8,2,9,2,6,9,3],
             [8,2,5,7,3,7,3,8,6,2]])
    print('All Done! Time to check!')
