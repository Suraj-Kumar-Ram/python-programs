#Given an array of integers and a sum, the task is to count all subsets of given array with sum equal to given sum.

#Input:
#The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an nteger n denoting the size of the array. The next line contains n space separated integers forming the array. The last line contains the sum.

#Output:
#Count all the subsets of given array with sum equal to given sum.

#Constraints:
#1<=T<=10^5
#1<=n<=10^5
#1<=a[i]<=10^5
#1<=sum<=10^5

#Example:
#Input:
#2
#6
#2 3 5 6 8 10
#10
#5
#1 2 3 4 5
#10

#Output:
#3
#3

arr = list(map(int,input("Enter elements seperated by a space : ").split()))
n = int(input("Enter a number : "))
c = 0
for t in arr:
    if(t==n):
        c= c+1
for i in range(len(arr)):
    a = arr[i]
    for j in range(i+1,len(arr)):
        a = a + arr[j]
        if(a == n):
            c = c+1
print(c)