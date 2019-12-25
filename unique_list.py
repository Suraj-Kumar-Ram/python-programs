def unique(k):
    c = list(set(k))
    return c
st = list(map(int,input(" Enter list elements : ").split()))
print("The input list : {}".format(st))
sl = unique(st)
sl.sort()
print("The unique list : {}".format(sl))