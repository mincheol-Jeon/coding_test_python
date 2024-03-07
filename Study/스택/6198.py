# 6198

# # 도시에는 N개의 빌딩이 있다
# # i번째 빌딩의 키가 h고 모든 빌딩은 일렬이고 오른쪽으로만 볼 수 있다
# # 관리인이 보는 방향이 정해져 있다
# # i번째 빌딩 관리인은 i+1, i+2,,, N까지 볼 수 있다
# # 자신이 위치한 빌딩보다 높거나 같으면 위치한 빌딩 <= 바라보는 빌딩

# # 옥상정원을 확인할 수 있는 총 수를 구하라

N = int(input())

# 문제지
heights = []

# 스택
stack = []

# 정답지
answer = [0] * N

# 문제집 배열에 정답을 집어 넣기
for i in range(N):
    heights.append(int(input()))

# 뒤집기
# heights = heights[::-1]

for i in range(len(heights)):
    # 만약에 스택이 비어있지 않고, 현재 빌딩이 비교하는 타워보다 높거나 같으면
    while stack and heights[i] >= heights[stack[-1]]:
        stack.pop()
        
    stack.append(i)
    answer[i] = len(stack) -1
    
print(sum(answer))
# ans = 0
# for i in range(len(heights)-1):
#     cnt = i + 1
#     while heights[i] > heights[cnt]:
#         ans += 1
#         cnt += 1
#         if cnt == len(heights):
#             break
# print(ans)
        
        
    
# print(sum(answer))

