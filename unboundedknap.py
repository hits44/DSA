def cutRod(coins, val):
    intmin = float("inf")-1
    # intmin=0
    n=len(coins)
    dp=[]
    for i in range(n+1):
        dp.append([intmin]*(val+1))
    
    for i in range(n+1):
        # if coins[i-1]!=
        dp[i][0]=0
    
    for i in range(1,val+1):
        if i%coins[0]==0:
            dp[1][i]=i//coins[0]
        else:
            dp[1][i]=intmin
    dp[0][0]=intmin
    for i in range(2,n+1): # price array
        for j in range(val+1): # n total weight
            if coins[i-1]<=j:
                dp[i][j]=min(
                    dp[i][j-coins[i-1]] +1,
                    dp[i-1][j]
                )
            else:
                dp[i][j]= dp[i-1][j]
    print(dp)
    return -1 if (dp[i][j]==intmin) else dp[i][j]
coins  =[17, 10, 5 ]
val = 6
print(cutRod(coins, val))