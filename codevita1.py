n = int(input("Enter the number of columns : "))
a = []
for i in range(3):
    b = list(input())
    a.append(b)
for i in range(n-2):
    if(a[0][i]=='#' and a[1][i]=='#' and a[2][i]=='#'):
       print("#",end="")
    else:
        if(a[0][i] == '*' and a[0][i+1] == '.' and a[0][i+2]=='*' and a[1][i]=='*' and a[1][i+1]=='*' and a[1][i+2]=='*' and a[2][i]=='*' and a[2][i+1]=='*' and a[2][i+2]=='*'):
            print("U",end="")
            i = i+2
        else:
            i = i+1