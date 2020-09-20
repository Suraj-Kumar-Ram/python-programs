def sub(arr):
    st = []
    for i in range(len(arr)):
        b = []
        for j in range(len(arr)):
            if(j!=i):
                b = []
                b.append(arr[i])
                b.append(arr[j])
                if((b in st)==False):
                    st.append(b)
    return(st)
arr = list(map(int,input("Enter list elements : ").split()))
st2 = sub(arr)
c = 0
for s in st2:
    if(s[0]^s[1]==0):
        c = c+1
print(c)