
def func(prices,n,ans,todo,res):
    l=len(prices)

    if n==l:
        print("return  ",n)
        ans=0
        return
    
    for i in range(n,l):
        print("i = ",i,"prices= ",prices,"n= ",n,"ans= ",ans,"todo= ",todo,"res = ",res)
        if todo=="buy":
            ans-=prices[i]
            todo="sell"
        elif todo=="sell":
            ans+=prices[i]
            todo="cool"
        elif todo=="cool":
            todo="buy"
        
        res[0]=max(res[0],ans)
        print("i = ",i,"prices= ",prices,"n= ",n,"ans= ",ans,"todo= ",todo,"res = ",res)

        func(prices,n+1,ans,todo,res)
        # ans=01

prices = [1,2,3]
n=0
ans=0
todo="buy"
res=[float("-inf")]

func(prices,n,ans,todo,res)
print(res)