# 구간 합 구하기 2
#  1 <= N <= 1024 
#  1 <= M <= 100,000

n, m = map(int,input().split()) # 표의 크기 N , 합을 구해야 하는 횟수 M

a = [[0] * (n+1)]
d = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    a_row = [0] + [int(x) for x in input().split()]
    a.append(a_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        d[i][j] = d[i-1][j] + d[i][j-1] + a[i][j] - d[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    res = d[x2][y2] - d[x2][y1-1] - d[x1-1][y2] + d[x1-1][y1-1]
    print(res)

