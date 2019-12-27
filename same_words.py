def animal_cracker(k):
    p=k.upper()
    c = list(p.split())
    if(c[0][0]==c[1][0]):
        return True
    else:
        return False
st = input("Enter a two-word sentence : ")
t = animal_cracker(st)
if(t==True):
    print("{} starts with two same words !!!!!!".format(st))
else:
    print("{} starts with different words.".format(st))