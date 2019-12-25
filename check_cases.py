def check(s):
    l=0
    for i in s:
        if(i.islower()):
            l+=1
    return l
n = input("Enter some sentence ( please enter only letters ) :")
low = check(n)
sen = list(n.split())
up = len(n)-(low + (len(sen) - 1))
print("No. of lower case characters : {}".format(low))
print("No. of upper case characters : {}".format(up))