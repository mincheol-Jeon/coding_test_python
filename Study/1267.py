# 1267

# 영식 요금제 구현
def youngsik(time):
    return (time//30 + 1) * 15
# 민식 요금제 구현
def minsik(time):
    return (time//60 + 1) * 15

n = int(input())
arr = list(map(int,(input().split())))

y = 0 # 영식 요금 값
m = 0 # 민식 요금 값
for i in arr:
    y += youngsik(i)
for j in arr:
    m += minsik(j)
    
if y > m: # 민식이가 더 싼 경우
    print('M',m)
elif y < m: # 영식이가 더 싼 경우
    print('Y',y)
elif y == m:
    print('Y M',m)
