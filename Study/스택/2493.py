# 2493
N = int(input())
arr = list(map(int,input().split()))
stack = []
answer = [0] * N

for i in range(N):
    # 스택이 비어있지 않고, 현재의 탑이 스택의 탑보다 높으면
    while stack and arr[i] > arr[stack[-1]]:
        stack.pop()
    
    # 스택이 비어있지 않다면 -> 현재 탑의 인덱스를 저장
    if stack:
        # 빛의 진행 방향이 왼쪽이므로, 가장 가까운 오른쪽이면 stack[-1]번 째여야 한다
        answer[i] = stack[-1] + 1
        
    stack.append(i)

print(*answer)