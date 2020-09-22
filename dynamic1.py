# fibonaci series using dynamic programming
def fibo(n,look):
    if(n<=1):
        look[n] = n
    if(look[n]==None):
        look[n] = fibo(n-1,look) + fibo(n-2,look)
    return(look[n])

n = int(input("Enter a number : "))
look = [None]*100
print(fibo(n,look))
       