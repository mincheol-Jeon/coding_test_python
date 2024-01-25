# B3
arr = list(map(int,input().split()))
arr_ = list(map(int,input().split()))
arr__ = list(map(int,input().split()))
for i in [arr,arr_,arr__]:
    if i.count(0) == 4:
        print('D')
    elif i.count(0) == 3:
        print('C')
    elif i.count(0) == 2:
        print('B')
    elif i.count(0) == 1:
        print('A')
    elif i.count(0) == 0:
        print('E')

    