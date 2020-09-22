
def sub(inp,out):
    s = ""
    if(len(inp)==0):
        if(len(out)!=0):
            s = s+str(out)
        return(s)
    sub(inp[1:],out[:])
    if(len(out)==0):
        sub(inp[1:],inp[:1])
    elif(inp[0]>out[-1]):
        out = out + inp[0]
        sub(inp[1:],out[:])
        