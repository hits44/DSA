def coinChange( coins, amount: int) -> int:
    dp=[]
    n=len(coins)
    for i in range(n+1):
        dp.append([None]*(amount+1))
    
    for i in range(n+1):
        for j in range(amount+1):
            if i==0 or j==0:
                dp[i][j]=0
            
    for i in range(1,n+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                # print(i,j)
                dp[i][j]= min(
                    1+dp[i][j-coins[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][amount]

coins = [1,2,5]
amount = 11
x = coinChange(coins,amount)
print(x)