# STRING PAIRS ---> CODEVITA

def vowels(m):
    c = 0
    for i in m:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            c = c+1
    return(c)

def sub_pairs(k):
    r = 0
    for i in range(len(k)):
        for j in range(len(k)):
            if(j!=i):
                if(int(k[i]) + int(k[j]) == s):
                    r = r+1
                    k[i] = 0
                    k[j] = 0
    return(str(r))

n = int(input())
numbers = input().split()
k = {'0':"zero",'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine"}
v = []
for i in numbers:
    v.append(k[i])
s = 0
for i in v:
    s = s + vowels(i)
print(k[sub_pairs(numbers)])