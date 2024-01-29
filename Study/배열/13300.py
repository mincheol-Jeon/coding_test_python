# 13300

N, K = map(int,input().split(' '))
dic_ = {i : {j : 0 for j in range(1,7)} for i in range(2)}

room = 0

for i in range(N):
    S,G = map(int,input().split(" "))
    dic_[S][G] += 1
# 0 여자 1 남자

for i in dic_[0]:
    if dic_[0][i] % K != 0:
        room += (dic_[0][i] // K) + 1
    else:
        room += (dic_[0][i] // K)
        
for i in dic_[1]:
    if dic_[1][i] % K != 0:
        room += (dic_[1][i] // K) + 1
    else:
        room += (dic_[1][i] // K)
    

print(room)