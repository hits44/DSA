def kadane(a):
    l=len(a)

    maxsum = -1
    sum =0
    start=0
    end=0
    for i in range(l):
        sum = sum+a[i]
        if sum >maxsum:
            maxsum = max(sum,maxsum)
            end = i
        if sum <0:
            sum =0
            start = i+1
    return (maxsum,a[start:end+1])

a = [2,-3,4,5]
print(kadane(a))