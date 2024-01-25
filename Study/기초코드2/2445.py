# 2445

n = int(input())
rev = [i for i in range(n)][::-1]

for i in range(1,n+1):
    print('*' * i + ' '*(n-i)*2 + '*' * i)

for j in rev:
    print('*' * j + ' ' * (n-j)*2 + '*' * j)