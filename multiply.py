def multiply(k):
    pro=1
    for i in k:
        pro = pro*i
    return pro
num = list(map(int,input(" Enter list elements : ").split()))
print(" The entered list : {}".format(num))
p = multiply(num)
print("The product of list elements : {}".format(p))