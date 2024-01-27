# 1475
import sys
input =  sys.stdin.readline

cnt = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

num = int(input())

for i in str(num):
    cnt[int(i)] += 1
    
ans = 0
for i in cnt.keys():
    tmp = cnt[i]
    if i == 6 or i == 9:
        if tmp > ans:
            if tmp % 2 == 0:
                tmp = tmp//2
                ans = tmp
            else:
                tmp = tmp//2 + 1
                ans = tmp
    elif tmp > ans:
        ans = tmp
print(ans) # 반례 166995 
