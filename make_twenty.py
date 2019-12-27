def twenty(a,b):
    if((a+b)==20 or a==20 or b==20):
        return True
    else:
        return False
num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
c = twenty(num1,num2)
if(c==True):
    print("Sum of {} and {} makes 20 OR either one of them is 20".format(num1,num2))
else:
    print("{} and {} does not make 20".format(num1,num2))