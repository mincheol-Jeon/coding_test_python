# 10093
A,B = map(int,input().split())
N = max(A,B)
M = min(A,B)
arr = [i for i in range(M+1,N)]
if N-M <= 1:
    print(0)
else:
    print(N-M-1)
    print(*arr, end = ' ')