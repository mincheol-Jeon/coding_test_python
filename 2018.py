# 투 포인터
import sys
input = sys.stdin.readline

n = int(input())

start_index = 1
end_index = 1
sum = 1
cnt = 0
while end_index != n+1:
    if sum == n:
        cnt += 1
        end_index += 1
        sum += end_index
        

    elif sum < n:
        end_index += 1
        sum += end_index
        
    
    else:
        sum -= start_index
        start_index += 1
        
        
print(cnt)