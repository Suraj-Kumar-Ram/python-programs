def path(mat1,mat2):
    if(mat2>mat1 and mat2 == mat1 +1):
        return(1)
    else:
        return(0)

def position(mat,mini):
    pi = 0
    pj = 0
    c = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(mat[i][j]==mini):
                pi = i
                pj = j
    c.append(pi)
    c.append(pj)
    return(c)

def matrix(m,n):
    c = []
    for i in range(n):
        k = []
        for j in range(n*i,n*i+n):
            k.append(m[j])
        c.append(k)
    return(c)
mat = list(map(int,input("Enter list elements : ").split()))
num1 = int(input("Enter the order of matrix : "))
mat2 = matrix(mat,num1)
mini = min(min(mat2))
pos = position(mat2,mini)
i = pos[0]
j = pos[1]
h = 0
while(path(mat2[i][j],mat2[i+1][j])!=0 or path(mat2[i][j],mat2[i][j+1])!=0 or path(mat2[i][j],mat2[i-1][j])!=0 or path(mat2[i][j],mat2[i][j-1])!=0):
    if(i==0 and j==0):
        if(path(mat2[i][j],mat2[i+1][j])!=0):
            h = h + 1
            i = i+1
        if(path(mat2[i][j],mat2[i][j+1])!=0):
            h = h+1
            j = j+1
    if(i==num1-1 and j==num1-1):
        if(path(mat2[i][j],mat2[i-1][j])!=0):
            h = h+1
            i = i-1
        if(path(mat2[i][j],mat2[i][j-1])!=0):
            h = h+1
            j = j-1
    if(i==0):
        if(path(mat2[i][j],mat2[i+1][j])!=0):
            h = h+1
            i = i+1
    if(i!=num1-1):
        if(path(mat2[i][j],mat2[i+1][j])!=0):
            h = h+1
            i = i+1
    if(i!=0):
        if(path(mat2[i][j],mat2[i-1][j])!=0):
            h  = h+1
            i = i-1
    if(j!=num1-1):
        if(path(mat2[i][j],mat2[i][j+1])!=0):
            h = h+1
            j = j+1
    if(j!=0):
        if(path(mat2[i][j],mat2[i][j-1])!=0):
            h = h+1
            j = j-1
print(h)