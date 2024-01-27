# 1475

# 한 세트에는 0 ~ 9까지가 있다

arr = [0 for i in range(10)]

n = int(input())

for i in str(n):
    if i == "6" or i == "9": # '6' OR 6
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[int(i)] += 1
print(max(arr))

