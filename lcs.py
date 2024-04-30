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
        







def lcsubstr(a, b): # can also print 
    m = len(a)
    n = len(b)
    dp=[]

    for i in range(m+1):
        dp.append([0]*(n+1))

    ans=0
    res = ""
    maxres = ""
    for i in range(1,m+1): # price array
        for j in range(1,n+1):

            if a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                res+=a[i-1]
                # print(res)
                if dp[i][j]>ans:
                    ans = dp[i][j]
                    # maxres=res
            # else:
            #     res+=" "

    # print(dp)
    return ans,res
a= "ababa"
b="cbbcad"
# b = "ababcde"
print(lcsubseq(a,b))
