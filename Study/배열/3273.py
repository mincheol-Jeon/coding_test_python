# 3273 (시간초과)

n = int(input())
arr = list(map(int,input().split(" ")))
sol = int(input())
ans = 0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == sol:
            ans += 1

print(ans)
