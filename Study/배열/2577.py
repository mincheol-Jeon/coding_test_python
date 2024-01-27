# 2577
res = 1

for i in range(3):
    res *= int(input())

arr = {i : 0  for i in range(10)}

for i in str(res):
    arr[int(i)] += 1    
    
print(*arr.values(),end='\n')