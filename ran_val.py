def ran_val(x,y,z):
    if(y<=x and x<=z):
        return 1
num = int(input("Enter the number :"))
low = int(input("Enter the lower limit :"))
high = int(input("Enter the upper limit :"))
c = ran_val(num,low,high)
if(c==1):
    print("{} is in range between {} and {} ".format(num,low,high))
else:
    print("{} is not within the range of {} and {} ".format(num,low,high))