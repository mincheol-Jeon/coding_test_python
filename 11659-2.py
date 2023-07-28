n,m = map(int,input().split())
arr = list(map(int,input().split()))
idx = 0 
sum = [None for i in range(n+1)]
sum[0] = 0
for s in range(1,len(arr)+1):
    idx += arr[s-1]
    sum[s] = idx
    
for k in range(3):
    i,j = map(int,input().split())
    print(sum[j]-sum[i-1])
    
