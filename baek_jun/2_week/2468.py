import sys

sys.setrecursionlimit(10000)

def dfs(h,y,x):
    visited[y][x] = True
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny<0 or nx<0 or ny>n-1 or nx>n-1: continue
        if visited[ny][nx] is False and adj[y][x] >h: dfs(h,ny,nx)
    return

n = int(input())
max_num = 0
adj = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    low = list(map(int,input().split()))
    adj.append(low)
    for j in low:
        if j > max_num:
            max_num = j

count = 0
result = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]
for i in range(1,max_num):
    for j in range(n):
        for k in range(n):
            if(adj[j][k] > i and visited[j][k] is False):
                dfs(i,j,k)
                count +=1
    result = max(result,count)
    count = 0
    visited = [[False] * n for _ in range(n)]
print(result)