#10804
arr = [i for i in range(1,21)]

for i in range(10):
    a,b = map(int,input("").split())
    tmp = arr[a-1:b]
    arr[a-1:b] = tmp[::-1]

print(*arr, end=' ')