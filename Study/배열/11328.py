# 11328

n = int(input())
ans = []

for _ in range(n):
    s1, s2 = input().split()
    # 문자열을 정렬하여 비교
    if sorted(s1) == sorted(s2):
        ans.append('Possible')
    else:
        ans.append('Impossible')

for result in ans:
    print(result)
