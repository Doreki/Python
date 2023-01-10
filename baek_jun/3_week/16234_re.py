import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(y,x):
    global count
    global sum

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= n or visited[ny][nx]==True:
            continue

        diff = abs(adj[y][x] - adj[ny][nx])
        if l<=diff<= r:
            visited[ny][nx] = True
            arr.append([ny,nx])
            sum+=adj[ny][nx]
            dfs(ny,nx)



n,l,r = map(int,input().split())

arr = []
adj = []
for _ in range(n):
    adj.append(list(map(int,input().split())))

dy = [0,-1,0,1]
dx = [1,0,-1,0]

visited = [[False] * n for _ in range(n)]

sum = 0
result = 0
flag = True
while True:
    flag=False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                arr.clear()
                visited[i][j] = True
                arr.append([i,j])
                sum = adj[i][j]
                dfs(i,j)
                if len(arr) == 1:continue
                avg = sum//len(arr)
                for a in arr:
                    y,x = a
                    adj[y][x] = avg
                    flag = True

    if flag==False:
        break

    result +=1

print(result)
