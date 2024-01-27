#  내가 처음 만든 답(정답)

import sys
input = sys.stdin.readline

sum = 0
cnt = 0
n,m = map(int,input().split())
a = list(map(int,input().split()))
s = [0] * n
c = [0] * m
for i in range(n):
    tmp = a[i]
    sum += tmp
    if sum % m == 0:
        cnt += 1
    s[i] = sum
    c[sum%m] += 1

for i in range(m):
    if c[i] > 1:
        cnt += (c[i] * (c[i] - 1) // 2)
print(cnt)


# 모범 답안

import sys 
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
s = [0] * n
c = [0] * m
cnt = 0
s[0] = a[0]
for i in range(1,n):
    s[i] = s[i-1] + a[i]

for i in range(n):
    t = s[i] % m
    if t == 0:
        cnt += 1
    c[t] += 1

for i in range(m):
    if c[i] > 1:
        cnt += (c[i] * (c[i]-1) // 2)
print(cnt)