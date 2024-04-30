x=2^1^3^4
c=0
k=1
while(x or k):

    if x%2 != k%2:
        c+=1
    x=x>>1
    k=k>>1

print(c)
