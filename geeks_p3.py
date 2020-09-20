#Input:
#2
#2 
#1 2
#3 
#1 3 5

#Output:
#4
#8

#Note: (a, b) and (b, a) are considered two separate pairs.

#Explanation:
#Test Case 1: 
#1: 01
#2: 10
#Bit difference in pair (1, 2): 2
#Bit difference in pair (2, 1): 2
#Hence, total Bit difference = 2 + 2 = 4

#Test Case 2: 
#1: 001
#3: 011
#5: 101
#Bit difference in pair (1, 3): 1
#Bit difference in pair (3, 1): 1
#Bit difference in pair (1, 5): 1
#Bit difference in pair (5, 1): 1
#Bit difference in pair (3, 5): 2
#Bit difference in pair (5, 3): 2
#Hence, total Bit difference = 1+1+1+1+2+2 = 8. 
def pair(m):  # Finds the pair of numbers
    k = []
    for i in range(len(m)):
        b = m[i]
        a = []
        for j in range(len(m)):
            if(b!=m[j]):
                a.append(b)
                a.append(m[j])
                k.append(a)
                a = []
    return(k)
def binary(m):
    k = []
    s = ""
    for t in m:
        s = ""
        while(t>0):
            s = s + str(t%2)
            t = t//2
        s = s[::-1]
        k.append(s)
    return(k)
n = list(map(int,input("Enter numbers seperated by space : ").split()))
