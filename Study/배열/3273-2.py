# 3273 (수정안)

n = int(input())
arr = list(map(int,input().split(" ")))
sol = int(input())
ans = 0

s = 0
e = -1

arr.sort()

while arr[s] != arr[e]:
    if arr[s] + arr[e] == sol:
        ans += 1
        s += 1
    elif arr[s] + arr[e] > sol:
        e -= 1
    else:
        s += 1

print(ans)
