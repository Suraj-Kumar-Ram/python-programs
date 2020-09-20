#Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

#For Example:
#If the matrix is    

#1 2 3
#4 5 6
#7 8 9
#The output should Return the following :

#[ 
#  [1],
#  [2, 4],
#  [3, 5, 7],
#  [6, 8],
#  [9]
#]
#i.e print the elements of array diagonally.

#Note: The input array given is in single line and you have to output the answer in one line only.
#Input:
#2
#2
#1 2 3 4
#3
#1 2 3 4 5 6 7 8 9
#Output:
#1 2 3 4
#1 2 4 3 5 7 6 8 9
def matrix(m,r):
    k = []
    for i in range(r):
        b = []
        for j in range(r):
            b.append(m[r*i+j])
        k.append(b)
    return(k)
n = int(input("Enter value of n : "))
a = list(map(int,input("Enter n*n space seperated values : ").split()))
m = matrix(a,n)
k = 0
h = []
while(k<=(2*(n-1))):
    for i in range(n):
        for j in range(n):
            if(i+j==k):
                h.append(m[i][j])
    k+=1
print("The obtained matrix is : ")
for t in h:
    print(t,end=" ")