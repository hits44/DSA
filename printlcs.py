def func(a,b,m,n):
    dp = []
    for  _ in range(m):
        dp.append([None]*n)

    for  i in range(m):
        dp[i][0]=0
    for j in range(n):
        dp[0][j]=0
    res=""

    for  i in range(1,m):
        for j in range(1,n):
            if a[i-1]==b[j-1]:
                res+=a[i-1]
                # dp[i][j]=1+dp[i-1][j-1]
            # else:
                # dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    print(res)    
    # print(dp[m-1][n-1])

a="acder"
b="abtter"
m=len(a)+1
n=len(b)+1

func(a,b,m,n)