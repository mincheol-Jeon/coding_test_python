import sys
input = sys.stdin.readline
print = sys.stdout.write
li = []
A = int(input())
for i in str(A):
    li.append(i)
for i in range(len(li)):
    swap = li.index(max(li[i:]))
    li[swap],li[i] = li[i],li[swap]

for i in li:
    print(i)