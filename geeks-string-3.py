# closing third bracket index

s = list(input("Enter a string : "))
n = int(input("Enter the index of opening third bracket : "))
c = 1
d = 0
for i in range(n+1,len(s)):
    if(c!=0):
        if(s[i] == ']'):
            c = c-1
        if(s[i] == '['):
            c = c+1
        d = d+1
    else:
        break
print(d+n)