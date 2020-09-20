#Example:
#Input:
#academy
#3
#Output:
#aca
def sub_str(m,n):
    k = []
    for i in range(len(m)):
        a = m[i:i+n]
        k.append(a)
    return(k)
def palin(m):
    n = ""
    for i in range(len(m)):
        n = n + m[len(m)-1-i]
    if(n==m):
        return(m)
    else:
        return(0)
st = input("Enter a word : ")
k1 = int(input("Enter the value of k : "))
arr = sub_str(st,k1)
c = []
for i in range(len(arr)):
    if(len(arr[i])==k1):
        k2 = palin(arr[i])
        if(k2!=0):
            c.append(k2)
for t in c:
    print(t,end = " ")