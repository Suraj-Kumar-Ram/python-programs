def check(ars,st,s):
    sf = ""
    sf = sf + ars.pop()
    c = 1
    while(sf!=st):
        for i in s:
            if(sf == i):
                sf = sf + i
                c= c+1
                
    
    

def sub(st):
    s = []
    for i in range(len(st)):
        st2 = st[0:len(st)-i]
        s.append(st2)
    s = s[::-1]
    return(s)
st = input("Enter a string : ")
sd = list(st)
sd = sd[::-1]
s = sub(st)
look = [None]*100
n = len(st)