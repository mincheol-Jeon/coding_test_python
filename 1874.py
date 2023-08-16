import sys
import time
input = sys.stdin.readline

N = int(input())
A = [0] * N 

stack = [] # 스택을 리스트로 구현
num = 1
answer = []
result = True


for i in range(N):
    A[i] = int(input())
    
t = time.time()

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)    
            num += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        n = stack.pop()
        if n > su:
            print('NO')
            result = False
            break
        else:
            answer.append('-')
if result:
    for i in answer:
        print(i)      