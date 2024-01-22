# B5
# map으로 받으면 각 변수로 정해진 유형대로 분할됌
N,X = map(int,input().split())
arr = list(map(int,input().split()))
for i in arr:
    if i < X:
        print(i, end=' ')