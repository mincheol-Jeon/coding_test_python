import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

ans = [-1 for i in range(N)]
stack = []

for i in range(N):
    while stack and (A[stack[-1]] < A[i]):
        ans[stack.pop()] = A[i]
    stack.append(i)
print(*ans)



# 17298

#크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
# 예를 들어, A = [3, 5, 2, 7]인 경우 
# NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

N = int(input())
arr = list(map(int,input().split()))
answer = [-1] * N
stack  = []
# i = 0 arr[0] = 3 , 스택 비어있음, 아래로 내려가서 append
# i = 1 arr[1] = 5, 스택 [3] 5 > 3 보다 크니까, 오큰수 기준이 변동 -> 정답[stack애서 pop] = 이번 오큰수 위치
for i in range(len(arr)):
    # 현재의 숫자가 스택의 마지막에 있는 것보다 크면 다음 오큰수 기준은 현재 숫자다
    # 따라서 스택을 빼주고 넣어줘야 한다
    while stack and arr[i] > arr[stack[-1]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
    
print(*answer)