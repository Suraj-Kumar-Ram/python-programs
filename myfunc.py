def myfunc(k):
    t=""
    for i in range(len(k)):
        if(i%2==0):
            t=t+k[i].upper()
        else:
            t=t+k[i].lower()
    return t
st = input("Enter sentence :")
print("Alternating the sentence cases........")
c = myfunc(st)
print(" The output sentence : {}".format(c))