import sys

sys.setrecursionlimit(10000)

def dfs(y,x):
    global result
    if y<0 or x<0 or y>n-1 or x>m-1: return False
    if adj[y][x] == 0 and visited[y][x] is False:

        visited[y][x] = True
        dfs(y+1,x)
        dfs(y-1,x)
        dfs(y,x+1)
        dfs(y,x-1)
        result +=1
        return True
    return False

n,m,t = map(int,input().split())

adj = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for _ in range(t):
    a,b,c,d = map(int,input().split())
    for i in range(n-d,n-b):
        for j in range(a,c):
            adj[i][j] = 1

count = 0
result = 0
arr = []
for i in range(n):
    for j in range(m):
        if(dfs(i,j)):
            count +=1
            arr.append(result)
            result = 0
print(count)
arr = sorted(arr)
for a in arr:
    print(a,end=" ")