# B3
arr = []
for i in range(7):
    arr.append(int(input()))

odd_arr = []

for i in arr:
    if i % 2 == 1:
        odd_arr.append(i)
if len(odd_arr) == 0:
    print(-1)
else:
    print(sum(odd_arr))
    odd_arr.sort()
    print(odd_arr[0])