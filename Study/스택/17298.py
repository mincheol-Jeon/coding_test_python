# 17298

#크기가 N인 수열 A = A1, A2, ..., AN이 있다. 
# 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
# 그러한 수가 없는 경우에 오큰수는 -1이다.
# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

N = int(input())
arr = list(map(int,input().split()))

ans = [-1] * N
stack = []

# 현재 숫자가 스택의 마지막 숫자보다 크면, 스택 속 숫자의 입장에서는 현재 숫자가 오큰수다
# -> 스택에서 pop 해야한다
# -> 그리고 이 검사는 stack이 차있는 동안 계속되야한다
for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)
print(*ans)