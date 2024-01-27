# 3273 (공간복잡도를 늘리고 시간복잡도를 줄인 해시맵 방법)
# CHATGPT의 도움을 받음

n = int(input())
arr = list(map(int, input().split()))
sol = int(input())

# 수열의 각 원소를 key로 가지고 있는 딕셔너리 생성
element_count = {}
for num in arr:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1

# 문제의 조건을 만족하는 쌍의 개수를 카운트
count = 0
for num in arr:
    complement = sol - num
    # 수열에서 빼고 남은 값(complement)이 딕셔너리에 존재하면 count에 그 값의 개수를 더함
    if complement in element_count:
        count += element_count[complement]
    # 현재 원소가 complement와 같은 경우에는 문제의 조건을 만족하는 (num, num) 쌍이 되므로 하나를 빼줌
    if num == complement:
        count -= 1 # """ 여기를 왜 빼야하는 걸까?"""

# 쌍의 개수는 문제의 조건을 만족하는 쌍을 두 번씩 세었으므로 2로 나누어야 함
print(count // 2) # """ 왜 2로 나눠야 할까?"""