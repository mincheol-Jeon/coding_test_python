n, m = map(int,input().split())
# a = [[0]*(n)]
a = [[0]*(n+1)]
s = [[0]*(n+1) for _ in range(n+1)]
# s = [[0]*(n) for _ in range(n)]

for _ in range(n):
    li = list(map(int,input().split()))
    li = [0] + li
    a.append(li)
for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j] = s[i-1][j] + s[i][j-1] + a[i][j] - s[i-1][j-1]
        
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])