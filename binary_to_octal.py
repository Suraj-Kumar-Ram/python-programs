def to_decimal(m):
    i = 0
    sum1 = 0
    while(m>0):
        k = m % 10
        sum1 = sum1 + k*(2**i)
        m = m // 10
        i+=1
    return sum1
n = int(input("Enter a binary number : "))
p = n
t = to_decimal(n)
sum2 = ""
a = []
while(t > 0):
    k2 = t % 8
    a.append(k2)
    t = t // 8
a = a[::-1]
for i in a :
    sum2 = sum2 + str(i)
print("The octal of {} is {}".format(p,sum2))