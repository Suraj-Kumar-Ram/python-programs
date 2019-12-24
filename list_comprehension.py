low = int(input("Enter the lower limit :"))
up = int(input("Enter the upper limit :"))
n = list(range(low,up+1))
t = [x**2 for x in n ]
for i in t:
    print(i)