# 1406 S2
right = []
left = list(input())
num = int(input())

for i in range(num):
    t = input()
    if 'P' in t:
        plus = t.split(' ')[1]
        left.append(plus)
        # plus가 특정 위치에 추가되어야함
    elif t == 'L':
        # 커서가 왼쪽으로 움직이기
        right.append(left.pop())
    elif t == 'B':
        left.pop()
        # 커서의 왼쪽 삭제하기
    elif t == 'D':
        left.append(right.pop())
        # 커서가 오른쪽으로 움직이기    
answer = left + right[::-1]
print(''.join(answer))