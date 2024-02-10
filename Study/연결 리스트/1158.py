# 1158

n, k = map(int, input().split())

# 1~n번 사람
people = [i for i in range(1,n+1)]
result = []

while people:
  for _ in range(k-1):
    people.append(people.pop(0))

  result.append(people.pop(0))
  
print("<", end="")
for i in range(len(result)-1):
  print(result[i], end=", ")
print(str(result[len(result)-1])+">")
