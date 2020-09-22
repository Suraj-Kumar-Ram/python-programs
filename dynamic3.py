st = []
def findsub(inp,out):
   if(len(inp)==0 ):
       if(len(out)!=0):
           st.append(out)
       return
   findsub(inp[1:],out[:])
   if(len(out)==0):
       findsub(inp[1:],inp[:1])
   elif(inp[0]>out[-1]):
       out.append(inp[0])
       findsub(inp[1:],out[:])

f = list(map(int,input("Enter list elements : ").split()))
l = []
length = []
findsub(f,l)
for i in st:
    length.append(len(i))
print(max(length))