def subsetsum(a):
    n=len(a)+1

    totalsum =0
    for i in a:
        totalsum+=i
    sum = 0
    if totalsum%2==0:
        sum = totalsum//2
    else: return False

    sum+=1
    dp=[]
    for i in range(n):
        dp.append([None]*sum)
    
    for i in range(sum):
        dp[0][i]=False
    # dp[0][0]=True
    
    for i in range(1,n):
        for j in range(1,sum):

            if a[i-1]<=j:
                dp[i][j]=(dp[i-1][j-a[i-1]] or dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n-1]

a=[1,5,11,5,]
print(subsetsum(a))




