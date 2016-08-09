
i = 0
j = 0

arr = [3, 1, 9, 8, 6, 4, 5, 7]

for i in range(len(arr)-1):
    for j in range(i,len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j+1],arr[j] = arr[j],arr[j+1]

print(arr)
