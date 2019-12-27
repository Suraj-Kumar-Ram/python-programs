def lesser_of_two_evens(a,b):
    if(a%2==0 and b%2==0):
        if(a<b):
            return a
        else:
            return b
    elif(a%2==0):
        return a
    elif(b%2==0):
        return b
    else:
        return 0
num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
c = lesser_of_two_evens(num1,num2)
if(c==0):
    print("The numbers {} and {} entered are not even.".format(num1,num2))
else:
    print("{} is the lesser even between the two numbers.".format(c))