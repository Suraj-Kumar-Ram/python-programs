#Given a vector of N positive integers and an integer X. The task is to find the frequency of X in vector.

#Input Format:
#First line of input contains number of testcases T. For each testcase there will be three lines. First line of which contains N, size of vector. Second line contains N positive integers seperated by space, and third line contains X, whose frequency is required.

#Output Format:
#For each testcase, print the frequency of X.

n = int(input("Enter the vector size : "))
arr = list(map(int,input("Enter array elements : ").split()))
x = int(input("Enter the number : "))
c = arr.count(x)
print(c)