def code(s):
    if s[0]=="0":
        return 0
    l=len(s)
    sing=[None]*l
    doubles=[None]*l
    # dp[0]=1
    sing[0]=1
    doubles[0]=0
    for i in range(1,l):
        if s[i]=="0":
            if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>=1 :
                doubles[i]=sing[i-1]+doubles[i-1]
                sing[i]=0
                # print(i,"ggg",sing[i])
            else: return 0    
        else:
            if int(s[i-1:i+1])<=26:
                sing[i]=sing[i-1]+doubles[i-1]
                doubles[i]=sing[i-1]
            else:
                sing[i]=sing[i-1]+doubles[i-1]
                doubles[i]=0
        # print(i,dp[i])
    # print(sing,doubles)
    return sing[l-1]+doubles[l-1]

print(code("10"))