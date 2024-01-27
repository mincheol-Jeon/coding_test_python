import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = list(map(int,input().split()))
s = [a[0] for _ in range(n)]
sum = 0
ans = 0
for i in range(n):
    # 합 배열 생성
    sum += a[i]
    s[i] = sum
    if s[i]%3 == 0:
        ans += 0
# 변경된 합 배열 생성    
s = [s[i]%3 for i in range(len(s))]
# 딱 나누어 떨어지는 갯수만큼 정답에 추가 
ans += s.count(0)
# 조합을 구현하는 방법, 발생하지 않은 나머지의 경우는 넘긴다
for i in range(m):
    if s.count(i) == 0:
        continue
    ans += int(s.count(i)*(s.count(i)-1)/2)
print(ans)

'''
이 방법은 시간을 초과했다.
이유는 내부연산 s.count(i)를 사용해서 그런 것으로 추정됌

막혔던 점은 나머지의 개수를 집계하는 배열을 하나 더 만들어야하는 이유를
떠올리지 못했다.
'''