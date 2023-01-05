import copy
import sys
sys.setrecursionlimit(10000)
def dfs(y,x):

        if y<0 or x<0 or y>=n or x>=m:
            return
        if visited[y][x] == False and adj[y][x] == 0:
            visited[y][x] = True
            dfs(y+1,x)
            dfs(y,x+1)
            dfs(y-1,x)
            dfs(y,x-1)
            arr.append((y,x))
            return
        return

n,m = map(int,input().split())

adj = []
arr=[]
dy = [0,-1,0,1]
dx = [1,0,-1,0]
for _ in range(n):
    adj.append(list(map(int,input().split())))

count = 0
tmp = []
while True:
    flag = True
    visited = [[False]*m for _ in range(n)]
    tmp = copy.deepcopy(adj)
    dfs(0,0)
    for a in arr:
        y = a[0]
        x = a[1]
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or nx<0 or ny>=n or nx>=m:
                continue
            adj[ny][nx] = 0
    for i in adj:
        for j in i:
            if j==1:
                flag=False
    count +=1
    if flag:
        break
cheese = 0
for a in tmp:
    for j in a:
        if j == 1:
            cheese+=1

print(count)
print(cheese)