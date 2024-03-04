# 1874
N = int(input())

stack = []
ans = []
find = True

# 초기 값 설정
now = 1
for _ in range(N):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        find = False
        
if not find:
    print('NO')
    
else:
    for i in ans:
        print(i)