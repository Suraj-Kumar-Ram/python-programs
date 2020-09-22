def coin_change(S,m,n,look):
    if(n==0):
        return(1)
    if(n<0):
        return(0)
    if(m<=0 and n>=1):
        return(0)
    look[n] = coin_change(S,m-1,n,look)+coin_change(S,m,n-S[m-1],look)
    return(look[n])