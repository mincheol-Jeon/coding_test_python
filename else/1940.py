import sys
import time

input = sys.stdin.readline

n = int(input())
m = int(input())
li = list(map(int,input().split()))
li = [0] + li

cnt = 0
start = 1
end = 1
t = time.time()
while start != n:
    sum = li[start] + li[end]
    if end == n:
        start += 1
        end = start
        
    elif sum != m:
        end += 1
        
    elif sum == m:
        cnt += 1
        end += 1

print('{:.9f}'.format(time.time()-t))      
print(cnt)
