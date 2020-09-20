n = int(input("Enter the length : "))
bride = list(input("Enter the brides : "))
groom = list(input("Enter the grooms : "))
a = 0
for i in range(n):
    k = bride[i]
    j = 0
    c = 0
    while(c<1 and j<n):
        if(groom[j] == k):
            c = c+1
            groom[j] = 0
        else:
            j = j+1
    if(j==n):
        break
for h in groom:
    if(h!=0):
        a = a+1
print((2*a))