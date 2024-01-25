# 2445

n = int(input())
rev = [i for i in range(1,n+1)][::-1]

for j in rev:
    print(' ' * (n - j) + '*' * (2 * j -1))
    
for i in range(1,n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))