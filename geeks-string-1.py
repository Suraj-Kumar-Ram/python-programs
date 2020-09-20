# PROGRAM FOR CASE SPECIFIC SORTING OF STRING

s = input("Enter a string : ")
ul = []
ll = []
for i in range(len(s)):
    if(s[i].isupper() == True):
        ul.append(s[i])
    else:
        ll.append(s[i])
st = ""
l = 0
u = 0
ll.sort()
ul.sort()
for i in range(len(s)):
    if(s[i].isupper() == True):
        st = st + ul[u]
        u = u+1
    else:
        st = st + ll[l]
        l = l+1
print(st)