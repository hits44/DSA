def lcsubseq(a, b):
    m = len(a)
    n = len(b)
    dp=[]

    for i in range(m+1):
        dp.append([0]*(n+1))

    for i in range(1,m+1): # price array
        for j in range(1,n+1):

            if a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    # print(dp)
    # return dp[m][n]
    maxres=""
    res=""
    i=m
    j=n
    while(i>0 and j>0):

        # print("i =",i ,"j= ",j,res)
        if a[i-1]==b[j-1]:
            res+=a[i-1]
            if len(res)>len(maxres):
                maxres=res

            i-=1
            j-=1
        else:
            # res =""
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1    
    return maxres[::-1]
        
a= "horse"
b="ros"

def editdistance(a,b,lcs):

    m=len(a)-1
    n=len(b)-1
    l=len(lcs)-1
    dell=0
    rep=0
    ins=0
    
    while(m>=0 and n>=0):

        if a[m]==b[n] :
            if a[m]==lcs[l] and l>=0:
                l-=1
            m-=1
            n-=1
        
        elif a[m]!=b[n] and a[m]!=lcs[l] and b[n]!=lcs[l]:
            if m!=n:
                dell+=1
                m-=1
            if m==n:
                rep+=1

        elif a[m]!=b[n]  :
            if a[m]==lcs[l] and b[n]!=lcs[l]:
                n-=1
            if a[m]!=lcs[l] and b[n]==lcs[l]:
                m-=1
                dell+=1
    print(dell,rep,ins)








lcs = (lcsubseq(a,b))
ans = editdistance(a,b,lcs)
print(ans)