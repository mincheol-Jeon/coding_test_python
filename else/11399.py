import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.sort()

sum = [A[i]*(N-i) for i in range(len(A))]

result = 0
for i in sum:
    result += i

print(result)