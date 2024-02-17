import sys

input = sys.stdin.readline

def push(number):
    array.append(int(number))
    return array

def pop_(array):
    if len(array) == 0:
        print(-1)
    else:
        print(array[-1])
        del array[-1]

def size(array):
    print(len(array))

def empty(array):
    if len(array) != 0:
        print(0)
    elif len(array) == 0:
        print(1)

def top_(array):
    if len(array) == 0:
        print(-1)
    else:
        print(array[-1])

iter_ = int(input())
array = list()

for i in range(iter_):
    func = input().split()

    if 'push' in func:
        _, number = func
        push(number)

    elif 'pop' in func:
        pop_(array)

    elif 'size' in func:
        size(array)

    elif 'empty' in func:
        empty(array)

    elif 'top' in func:
        top_(array)
