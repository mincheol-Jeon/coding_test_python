A,B,C = map(int,input().split())
dic = {"1" : 0, "2" : 0, "3" : 0, 
           "4" : 0, "5" : 0, "6" : 0}
for i in [A,B,C]:
    dic[str(i)] = dic[str(i)] + 1

for i in dic.keys():
    if dic[i] == 3:
        print(10000 + int(i) * 1000)
    elif dic[i] == 2:
        print(1000 + int(i) * 100)
    else:
       continue
if 3 not in dic.values() and 2 not in dic.values():
    print(max([A,B,C]) * 100)