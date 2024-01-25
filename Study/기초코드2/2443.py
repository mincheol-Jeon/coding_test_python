n = int(input())
li = [i for i in range(1,n+1)][::-1]

for i in li:
    print(' ' * (n-i) + '*' * (2*i - 1) )