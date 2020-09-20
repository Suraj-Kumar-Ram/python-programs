st1 = list(map(int,input("Enter n and d : ").split()))
n = st1[0]
d = st1[1]
arr = list(map(int,input("Enter the array elements : ").split()))
st2 = arr[:d]
arr2 = []
for i in range(d,len(arr)):
    arr2.append(arr[i])
for i in range(len(st2)):
    arr2.append(st2[i])
print(arr2)