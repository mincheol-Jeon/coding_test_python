import sys
input = sys.stdin.readline

N = int(input())
stack = [i for i in range(1,N+1)]
stack.reverse()
while len(stack) != 1:
    stack.pop()
    bottom = stack.pop()
    stack.insert(0,bottom)

print(*stack)