# 1406 S2
from sys import stdin
left = list(input())
right = []

for i in range(int(input())):
    t = list(stdin.readline().split())
    if t[0] == 'P':
        left.append(t[1])
    elif t[0] == 'L' and left:
        right.append(left.pop())
    elif t[0] == 'B'and left:
        left.pop()
    elif t[0] == 'D' and right:
        left.append(right.pop())
          
answer = left + right[::-1]
print(''.join(answer))