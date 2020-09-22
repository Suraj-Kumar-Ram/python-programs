# minimum number of changes required to convert string1 to string2 e.g: geek, gesek output: 1 since just inserting s

def least(str1,str2,m,n):
    if(m==0):
        return(n)
    if(n==0):
        return(m)
    if(str1[m-1]==str2[n-1]):
        return(least(str1,str2,m-1,n-1))
    return(1+min(least(str1,str2,m,n-1),least(str1,str2,m-1,n),least(str1,str2,m-1,n-1)))