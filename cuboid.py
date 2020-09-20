# hacker rank question python

x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))
z = int(input("Enter value of z : "))
n = int(input("Enter value of n : "))
k = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k)!=n)]
k.sort()
print(k)