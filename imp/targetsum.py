def subsetsum(a,sum):
    dp = []
    n = len(a)
    # print(sum)
    # no of zeros
    # zeros = 0
    # for i in a:
    #     if i==0:
    #         zeros+=1
    # zerossubseq = pow(2,zeros)

    for i in range(n+1):
        dp.append([None]*(sum+1))

    for i in range(sum+1):
        dp[0][i]=0
    for i in range(n+1):
        dp[i][0]=1
    # print(dp)
    # if a[0]==0: 
    #     dp[0][0]=2   
    for i in range(1,n+1):
        for j in range(0,sum+1):
            # if (j==0 ):
            #     dp[i][j]==pow(2,i)
            if a[i-1]<=j:
                dp[i][j] = dp[i-1][j-a[i-1]] + dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    # print(max(dp))
    print(dp)
    # if zeros:
    #     return dp[n][sum]*zerossubseq 
    return (dp[n][sum])

def tsum(a,target):
    n=len(a)
    ranges = 0
    for i in (a):
        ranges+=i
    print("yoo",ranges,target)
    
    if(ranges < target) :return 0
    if((ranges+target)<0 or ((ranges+target) % 2) != 0): return 0
    
    summ = (ranges+target)//2
    # print("rr",ranges,summ)
    ans = subsetsum(a,summ)
    return ans

def rectsum(a,n,target):
    if n==0 and target ==0:
        return 1
    elif (n ==0 ) :
        return 0
    

    return rectsum(a,n-1,target-a[n-1])+rectsum(a,n-1,target+a[n-1])

def rsum2(a,n,sum):
    if n==0 and sum==0:
        # print("got it n= ",n)
        return 1
    elif n==0 :
        return 0
    return rsum2(a,n-1,sum-a[n-1])+rsum2(a,n-1,sum+a[n-1])


a= [0,0,0,0,0,0,0,0,1]
s=1
# a = [3,5,6,7]
# s = 9
a=[1,5,11,5]
s=11
# a=[0,0,0,0,0,1]
# a=[0,0,0,0,0,0,0,0,1]
# s=1

a=[1,1,1]
target = 1

print(rsum2(a,len(a),s))