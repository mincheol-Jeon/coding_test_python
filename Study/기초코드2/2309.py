#2309
arr = []
for i in range(9):
    num = int(input())
    arr.append(num)

res = sum(arr)

fake = []

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if len(fake) == 2:
            continue
        if res - arr[i] - arr[j] == 100:
            fake.append(arr[i])
            fake.append(arr[j])

arr.sort()

for i in arr:
    if i in fake:
        continue
    print(i)

