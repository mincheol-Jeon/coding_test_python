n = int(input())
m = int(input())
li = list(map(int,input().split()))
li = [0] + li
cnt = 0
start = 1
end = 1

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

        
print(cnt)
