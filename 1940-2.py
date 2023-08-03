import sys
import time

input = sys.stdin.readline

n = int(input())
m = int(input())
cnt = 0
li = list(map(int,input().split()))
t = time.time()
li.sort()


start = 0
end = n-1
while start < end:
    sum = li[start] + li[end]
    if sum > m:
        end -= 1
    elif sum < m:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1
print(cnt)
print('{:.9f}'.format(time.time()-t))