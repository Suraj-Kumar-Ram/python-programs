st = []
def sub(inp,out):
    if(len(inp)==0):
        if(len(out)!=0):
            st.append(out)
        return
    sub(inp[1:],out[:])
    if(len(out)==0):
        sub(inp[1:],inp[:1])
    elif(inp[0]>out[-1]):
        out.append(inp[0])
        sub(inp[1:],out[:])

s1 = list(input("Enter string 1 : "))
s2 = list(input("Enter string 2 : "))
ss1 = []
ss2 = []
sub(s1,[])
for i in st:
    ss1.append(i)
st = []
sub(s2,[])
for j in st:
    ss2.append(j)
c = 0
for i in ss1:
    if((i in ss2)==True):
        c = 0
        k = i
        break
s = ""
for y in k:
    s = s+y
print(s)