import collections
def bfs(y,x):
    deque = collections.deque()
    deque.append([y,x])
    visited[y][x] = 1
    while(deque):
        y,x = deque.popleft()
        dy = [0,-1,0,1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m :
                continue
            if visited[ny][nx] or adj[ny][nx] !=1:
                continue
            visited[ny][nx] = visited[y][x]+1
            deque.append([ny,nx])

n,m = map(int, input().split())
adj = []
for _ in range(n):
  adj.append(list(map(int, input())))
visited = [[0] * m for _ in range(n)]
bfs(0,0)
print(visited[n-1][m-1])


