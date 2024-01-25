# 2444

n = int(input())

rev = [i for i in range(n)][::-1]
for i in range(1,n+1):
    print(' ' * (n-i) + '*' * (2*i - 1))
    
for j in rev:
    print(' ' * (n-j) + '*' * (2*j -1))
