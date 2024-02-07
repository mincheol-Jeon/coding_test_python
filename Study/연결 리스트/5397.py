# 5397
for j in range(int(input())):
    arr = list(input())
    left = []
    right = []
    for i in arr:
        if i == '<':
            if not left:
                continue
            else:
                try:
                    right.append(left.pop())
                except:
                    continue
        elif i == '>':
            if not right:
                continue
            else:
                try:
                    left.append(right.pop())
                except:
                    continue
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    ans = left + right[::-1]
    print(''.join(ans))           
            
