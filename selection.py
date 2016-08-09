a = [100, 2, 444, 10,223, 8 , 222]

for i in range(len(a)):
    print(i)
    temp = i
    for j in range(i,len(a)):
        print(temp,a[temp])
        if a[j] < a[temp]:
            temp = j
    print(temp,a[temp])
    a[i],a[temp] = a[temp],a[i]
    # for j in range(len(a)-i):
    #     if a[j] > a[temp]:
    #         temp = j
    # a[len(a)-1-i],a[temp] = a[temp],a[len(a)-1-i]


print(a)
