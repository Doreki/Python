import copy
import itertools
import sys
sys.setrecursionlimit(10000)
def dfs(y,x):
    if y<0 or x<0 or y>=n or x>=m or v[y][x]:
        return
    if tmp[y][x]==1:
        return
    v[y][x]=True
    tmp[y][x]=2
    dfs(y+1,x)
    dfs(y,x+1)
    dfs(y-1,x)
    dfs(y,x-1)

n,m = map(int,input().split())
a = []
comb = []
vir = []
dy = [0,-1,0,1]
dx = [1,0,-1,0]
v = [[False] * m for _ in range(n)]
for _ in range(n):
    a.append(list(map(int,input().split())))


for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            comb.append([i,j])
        elif a[i][j]==2:
            vir.append([i,j])


comb = list(itertools.combinations(comb,3))
count = 0
ans = 0
for com in comb:
    tmp = copy.deepcopy(a)
    for c in com:
        y,x = c
        tmp[y][x] = 1
    for vi in vir:
        y,x = vi
        dfs(y,x)
    for i in tmp:
        for j in i:
            if j==0:
                count+=1
    ans = max(ans,count)
    count=0
    v = [[False] * m for _ in range(n)]
print(ans)

