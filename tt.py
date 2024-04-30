
def memo(a):

    l =len(a)
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(l)]

    def func(i,todo,cap):
        if i==l or cap ==0:
            return  0
        if dp[i][todo][cap]!=-1:
            return dp[i][todo][cap]
        prof=0
        if  todo ==0:
            prof= max(
                func(i+1,0,cap),
                func(i+1,1,cap)-a[i]
                )
        elif todo ==1:
            prof=  max(
                func(i+1,1,cap),
                func(i+1,0,cap-1)+a[i]
                )
        dp[i][todo][cap] = prof
        return prof

    return func(0,0,2)

def cool(a):

    l =len(a)
    dp = [[-1 for _ in range(3)] for _ in range(l)]

    def func(i,todo):
        if i==l :
            return  0
        
        if dp[i][todo]!=-1:
            return dp[i][todo]
        prof=0
        
        if  todo ==0: # buy
            prof= max(
                func(i+1,0),
                func(i+1,1)-a[i]
                )
        elif todo ==1: # sell
            prof=  max(
                func(i+1,1),
                func(i+1,2)+a[i]
                )
        elif todo ==2:
            prof=  max(
                func(i+1,0),
                func(i+1,0)
                )
        dp[i][todo] = prof
        return prof

    return func(0,0)

def maxProfit(prices):
    n = len(prices)
    
    # Create a 3D DP table with dimensions (n) x 2 x 3 and initialize it with -1 values
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
    
    def getAns(ind, buy, cap):
        # Recursive function to calculate the maximum profit
        
        if ind == n or cap == 0:
            return 0  # Base case: If we have reached the end of the array or used up all transactions, return zero profit
        
        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]  # If the result is already computed, return it
        
        profit = 0
        
        if buy == 0:
            # We can buy the stock
            profit = max(0 + getAns(ind + 1, 0, cap), -prices[ind] + getAns(ind + 1, 1, cap))
        elif buy == 1:
            # We can sell the stock
            profit = max(0 + getAns(ind + 1, 1, cap), prices[ind] + getAns(ind + 1, 0, cap - 1))
        
        dp[ind][buy][cap] = profit  # Store the result in the DP table
        return profit

    return getAns(0, 0, 2) 
prices = [0,5,5,6,2,1,1,3]
prices = [3,3,5,0,0,3,1,4]
prices=[1,2,4,2,5,7,2,4,9,0]
prices = [3,3,5,0,0,3,1,4]
prices=[1,2,3,0,2]
# print(maxProfit(prices))
print(cool(prices))