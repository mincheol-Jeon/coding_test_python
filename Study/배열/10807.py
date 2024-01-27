# 10807
ans = 0
N = int(input())
arr = list(map(int,input().split(" ")))
sol = int(input())

for i in arr:
    if sol == i:
        ans += 1
print(ans)