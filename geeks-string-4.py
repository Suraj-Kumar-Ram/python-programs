# PRACTICE CODE

"""
Pappu is confused between 6 & 9 . He works in billing department of abc company and his work is to return the remaining amount to the customers. If actual remaining amount is given we need to find the maximum possible extra amount given by the pappu to the customers.

For ex:- actual remaining amount = 56

so, maximum possible extra amount =  (59 - 56 ) = 3
"""
s = list(input("Enter the remaining amount : "))
s2 = s[::]
st1 = ""
st2 = ""
for i in range(len(s)):
    if(s[i] == '6'):
        s2[i] = '9'
    if(s[i] == '9'):
        s2[i] = '6'
for i in range(len(s2)):
    st2 = st2 + s2[i]
    st1 = st1 + s[i]
m1 = max(int(st1),int(st2))
m2 = min(int(st1),int(st2))
print(m1-m2)