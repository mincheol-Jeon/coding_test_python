# 10773

number = int(input())
stack = []
 
for i in range(number):
    n = int(input())
    if n == 0:
        del stack[-1]
    else:
        stack.append(n)
print(sum(stack))