def question4(T, r, n1, n2):
    n1_ps = []
    while n1 != r:
        n1 = parent(T, n1)
        n1_ps.append(n1)
    if len(n1_ps) == 0:
        return -1
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in n1_ps:
            return n2
    return -1
    
    
def parent(T, n):
	#return parent of n if it exists, otherwise return -1
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return -1


print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)