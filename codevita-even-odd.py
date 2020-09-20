# EVEN ODD ---> CODEVI
fact = lambda f : f and f*fact(f-1) or 1

st = list(map(int,input("Enter the values : ").split()))
low = st[0]
high = st[1]
k = int(input("Enter value of k : "))
arr = [i for i in range(low,high+1)]
even = len(list(filter(lambda e : (e%2==0),arr)))
odd = len(list(filter(lambda e : (e%2!=0),arr)))
s = even**k
sec1 = lambda m : (m**k) and (k%2==0)
arr2 = [i for i in range(2,k+1,2)]
sec2 = lambda m : m and m+(fact(k)//(fact(g))*fact(k-g)) and (g%2==0),arr
s = s+sec1(k)+sec2(k)