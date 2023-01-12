import sys

sys.setrecursionlimit(10000)

def dfs(y,x,depth):
    if y<0 or x<0 or y>=n or x>=n or v[y][x]:
        return False
    if a[y][x] > depth:
        v[y][x]=True
        dfs(y+1,x,depth)
        dfs(y,x+1,depth)
        dfs(y-1,x,depth)
        dfs(y,x-1,depth)
        return True
    return False

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
v = [[False] * n for _ in range(n)]
count =0
result = 1
for k in range(1,101):
    for i in range(n):
        for j in range(n):
            if dfs(i,j,k):
                count+=1
    result = max(result,count)
    count = 0
    v = [[False] * n for _ in range(n)]
print(result)

