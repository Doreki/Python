import collections

def dfs(y,x):

    for i in range(4):
        ny = dy[i]+y
        nx = dx[i]+x

        if ny<0 or nx<0 or ny>=n or nx>=m or visited[ny][nx]:
            continue
        if a[ny][nx] in alpa:
            continue
        visited[ny][nx] = visited[y][x]+1
        alpa.append(a[ny][nx])
        dfs(ny,nx)


n,m = map(int,input().split())
a = []
alpa = []
dy = [0,-1,0,1]
dx = [1,0,-1,0]
flag = False
visited = [[0]*(m) for _ in range(n)]
for _ in range(n):
    a.append(list(input()))
count = 0
visited[0][0] = 1
alpa.append(a[0][0])
dfs(0,0)

for i in visited:
    for j in i:
        print(j,end=" ")
    print()
