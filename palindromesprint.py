def pal(s):

        l = len(s)
        
        # odd pals
        res= []
        for idx in range(l):
            i=idx
            j=idx
            while(i>=0 and j<l):

                if s[i]==s[j]:
                    res.append(s[i:j+1])
                    i-=1
                    j+=1
                else: break
            
            i=idx
            j=idx+1
            while(i>=0 and j<l):

                if s[i]==s[j]:
                    print("i = ",i,"j = ",j, s[i:j+1])
                    res.append(s[i:j+1])
                    i-=1
                    j+=1
                else:
                    break

        return res
print(pal("aaa"))

