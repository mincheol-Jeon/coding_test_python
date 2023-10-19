N, M = map(int,input().split())
arrive = False

A = [[] for _ in range(N+1)] # 인접 리스트 
visited = [False] * (N+1) # 노드 방문기록

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True # 현재 지점을 방문했기 때문에 True
    for i in A[now]: # 현재 방문 노드와 연결된 엣지를 확인하고자 인접 리스트를 확인
        if not visited[i]: # 연결된 엣지를 순회할 때 방문하지 않았다면
            DFS(i, depth + 1) # 재귀 호출하면서 깊이를 1 증가
        # visited[now] = False # 이 부분이 이해가 안감
    
for _ in range(M): # 먼저 양방향 엣지 개수만큼 입력받아 인접 리스트에 추가해줘야함
    s, e = map(int,input().split())
    A[s].append(e) # 양방향 엣지이므로 양쪽에 더하기
    A[e].append(s) # ""
    
for i in range(N):
    DFS(i,1)
    if arrive: # 깊이 5만큼에 도착했다면
        break
if arrive:
    print(1)
else:
    print(0)