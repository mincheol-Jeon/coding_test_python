# 10808
from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)
arr = {i : 0 for i in alphabet_list}

s = input()
for i in s:
    arr[i] += 1
print(*arr.values(),end=' ')