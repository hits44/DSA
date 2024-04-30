s = "applepenapple"
s="bb"
wordDict = ["apple","pen"]
wordDict =["a","b","bbb","bbbb"]

s= "a"
wordDict=["b"]

def func(s,wordDict):
    # smap = {}
    # for ch in s:
    #     smap[ch] = smap.get(ch,1)+1
    # for word in wordDict:
    #     while word in s:
    #         s=s.replace(word,"",1)
    wordDict = sorted(wordDict)
    newword =[]
    for word in wordDict:
        if word  in s:
            newword.append(word)
    wordDict = newword
    if not wordDict :return False
    run =True
    while run:
        for word in wordDict:
            if word not in s:
                run = False
            s=s.replace(word,"",1)
    print(s,len(s))
    return not len(s)

print(func(s,wordDict))
# xx = sorted(["car","ca","rs"])
# print(xx)
# print(s[start:end])

