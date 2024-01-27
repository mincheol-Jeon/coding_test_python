# 1919
from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)
arr = {i : 0 for i in alphabet_list}
arr_ = {i : 0 for i in alphabet_list}

s = input()
for i in s:
    arr[i] += 1
s_ = input()
for i in s_:
    arr_[i] += 1

a = list(arr.values())
b = list(arr_.values())
ans = 0

for i in range(len(a)):
    ans += abs(a[i] - b[i])
    
print(ans)