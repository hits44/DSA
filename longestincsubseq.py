

def func(a,op,c):

    if not a: # check if affecting the real a\
        # print("nnnn",(op))
        return len(op)
    print("a = ",a," op= ",op)
    c[0]+=1
    # anew = a
    if not op or a[0]>(a[-1]):
        # print("a0 = ", a[0], "op  ",int(op1[-1]))
        op1=op.copy()
        # print("ooooo")
        op1.append(a[0])
        # val1=0
        val1 = func(a[1:],op1,c)
    else:
        val1 = 0
    return  max(val1 , func(a[1:],op,c))
    # return max(val1,val2)


def liss(a):
    l=len(a)

    mindp = [None]*l
    lis = [None]*l

    mindp[0]=-1
    lis[0]=1

    for i in range(1,l):
        # currentsmaller = a[i]
        maxlis = 0
        for j in range(0,i):
            if a[j]<a[i] and lis[j]> maxlis:
                # currentsmaller=a[j]
                maxlis =lis[j]
        # mindp[i]=currentsmaller
        lis[i]=maxlis+1
    print(lis)
        



a= [1,2,1,4,3,5]
# a=[1,2,3,5,6,7]
# a=[10,9,2,5,3,7,101,18]
# a=
print(liss(a))
