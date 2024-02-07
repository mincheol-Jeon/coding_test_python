for j in range(int(input())):
    arr = list(input())
    left = []
    right = []
    for i in arr:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    ans = left + right[::-1]
    print(''.join(ans))