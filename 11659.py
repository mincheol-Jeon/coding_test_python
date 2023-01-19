# 구간 합 구하기 1
# 1 <= N <= 100,000 1번째 줄 # 숫자 개수
# 1 <= M <= 100,000 1번째 줄 # 질의 개수
# 시간 제한 0.5초 -> O(N) 1천만번, 100,000^2로는 불가능, O(N^2)은 안됌 

# # 내 풀이
N , M = map(int,input().split()) # 숫자 개수 , # 질의 개수
arr = [i for i in range(1,int(N+1))]
arr.reverse()
temp = 0 # 부분합을 더하는 변수
part_sum = [0] # 부분합을 저장하는 변수 # 처음에는 아무것도 더하지 않았으니 부분합은 0이다

for i in arr:
    temp += i
    part_sum.append(temp)

for i in range(M):
    start , end = map(int,input().split()) # 부분합이 시작되는 곳과 끝나는 곳을 저장하는 변수
    print(part_sum[end] - part_sum[start-1])
          
    
    

