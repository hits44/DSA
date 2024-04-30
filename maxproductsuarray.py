def prod(a):
    l=len(a)

    tp= [None]*l
    tpp = [None]*l
    tp[0]=a[0]
    tpp[0]= 1 if a[0]<0 or a[0]==0 else a[0]
    for i in range(1,l):
        if tp[i-1]==0:
            tp[i]=1*a[i]
        else:
            tp[i]=tp[i-1]*a[i]
            
        
        if a[i]<0 or a[i]==0:
            tpp[i]=1
            # tp[i]=1
        else: 
            tpp[i]=tpp[i-1]*a[i]
    
    tppmax = max(tpp)
    tpmax = max(tp)
    res = 0
    if tppmax>1:
        res = max(tppmax,tpmax)
    else:
        res=tpmax
    return res

a=[2,3,-2,4]
b=list(reversed(a))
res = max(prod(a),prod(b))
print(res)