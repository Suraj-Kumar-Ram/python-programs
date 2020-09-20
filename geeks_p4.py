#Input

#2
#5
#abaab
#7
#abbaeae

#Output

#3
#4

#Explanation:

#Test Case 1
#Input : str = "abaab"
#Output: 3
#All palindrome substring are : "aba" , "aa" , "baab"

#Test Case 2
#Input : str = "abbaeae"
#Output: 4
#All palindrome substring are : "bb" , "abba" ,"aea","eae"

def palin(m):
    if(len(m)>1):
        n = m[::-1]
        if(n==m):
            return(1)
        else:
            return(0)
    else:
        return(0)

st = input("Enter a word")
s = ""
c = 0
for i in range(len(st)-1):
    a = st[i]
    s = a
    for j in range(i+1,len(st)):
        s = s+st[j]
        if(palin(s)!=0):
            c = c+1
print(c)