import sys
input = sys.stdin.readline

N = int(input())
# 스타트 포인터와 엔드 포인터 만들어주기
start = 0
end = 1
# 가능한 가지수를 저장하는 변수
cnt = 0 
# 합을 저장할 변수
sum = 0
# 포인터가 움직일 배열 생성
li = [i for i in range(1,N+1)]
sum = li[start] + li[end]

while end != N:
    if sum < N:
        end += 1
        sum += li[end]
        
    elif sum > N:
        sum -= li[start]
        start += 1
        
    elif sum == N:
        cnt += 1
        end += 1
        if end < N:
            sum += li[end]
    
print(cnt)