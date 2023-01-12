import sys
sys.setrecursionlimit(10000)
def dfs(y,x):
    global result
    if y<0 or x<0 or y>=n or x>=m or v[y][x]:
        return False
    if a[y][x] == 0:
        result +=1
        v[y][x] = True
        dfs(y+1,x)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y,x-1)
        return True
    return False
n,m,k = map(int,input().split())
a = [[0] * m for _ in range(n)]
v = [[False] * m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            a[i][j] = 1
count = 0
result = 0
arr = []
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            count+=1
            arr.append(result)
            result = 0

arr.sort()
print(count)
print(*arr)