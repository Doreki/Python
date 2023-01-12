import collections


def bfs(y,x):
    q = collections.deque([[y,x]])
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        # print(y,x)
        for i in range(4):
            ny = dy[i]+y
            nx = dx[i]+x
            if ny<0 or nx<0 or ny>=n or nx>=m:
                continue
            if visited[ny][nx]:
                continue
            if a[ny][nx]==0:
                continue
            visited[ny][nx] = visited[y][x]+1
            q.append([ny,nx])
    return visited[n-1][m-1]


n,m = map(int,input().split())
a = []
dy = [0,-1,0,1]
dx = [1,0,-1,0]
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    a.append(list(map(int,input())))
print(bfs(0,0))