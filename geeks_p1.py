n = int(input("Enter digit : "))
a = list(map(int,input("Enter upper and lower limit : ").split()))
l = a[0]
u = a[1]
d=0
for i in range((l+1),u):
    k = str(i)
    c = list(k)
    for j in c:
        if(int(j)==n):
            d = d+1
    