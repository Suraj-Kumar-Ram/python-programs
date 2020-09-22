st = []
def printsub(arr,i,sub):
    if(i==len(arr)):
        if(len(sub)!=0):
            st.append(sub)
    else:
        printsub(arr,i+1,sub)
    return