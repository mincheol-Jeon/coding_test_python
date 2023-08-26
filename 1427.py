import sys
input = sys.stdin.readline
print = sys.stdout.write
li = []
A = int(input())
for i in str(A):
    li.append(i)
li.sort(reverse=True)
for i in li:
    print(i)