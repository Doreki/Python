from collections import deque


def bfs(y,x):
    if adj[y][x] == 'W':
        return
    visited[y][x] = True
    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or ny>=n or nx>=m or visited[ny][nx] == True or adj[ny][nx]=='W':
                continue

            dis[ny][nx] =dis[y][x]+1
            visited[ny][nx] = True
            q.append([ny,nx])



n,m = map(int,input().split())
adj = []
dy = [-1,0,1,0]
dx = [0,1,0,-1]
for _ in range(n):
    adj.append(list(input()))

visited = [[False]*m for _ in range(n)]
dis = [[0]*m for _ in range(n)]
tmp = 0
max_num = 0
result = 0
for i in range(n):
    for j in range(m):
        bfs(i,j)

        for k in dis:
            for j in k:
                tmp = j
                max_num = max(max_num,tmp)
        result = max(max_num,result)

        visited = [[False] * m for _ in range(n)]
        dis = [[0] * m for _ in range(n)]
        max_num = 0
print(result)