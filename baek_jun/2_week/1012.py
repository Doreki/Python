import sys

sys.setrecursionlimit(10000)

def dfs(y,x):
    if y<0 or x<0 or y>n-1 or x>m-1: return False
    if adj[y][x] == 1 and visited[y][x] is False:

        visited[y][x] = True
        dfs(y+1,x)
        dfs(y-1,x)
        dfs(y,x+1)
        dfs(y,x-1)
        return True
    return False

t = int(input())

for _ in range(t):
    n,m,k = map(int,input().split())
    adj = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0
    for _ in range(k):
        y,x = map(int,input().split())
        adj[y][x] = 1
    for i in range(n):
        for j in range(m):
            if(dfs(i,j)) : count +=1
    print(count)