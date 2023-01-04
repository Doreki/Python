from itertools import combinations
import sys
import copy

sys.setrecursionlimit(10000)
def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return
    if tmp[x][y] != 1 and visited[x][y] is False:
        visited[x][y] = True
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        tmp[x][y] = 2

n,m = map(int,input().split())

adj = []

for _ in range(n):
    adj.append(list(map(int,input().split())))

comb = []
vir = []
visited=[[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if adj[i][j] == 0:
            comb.append(i*m+j)
        if adj[i][j] == 2:
            vir.append(i*m+j)
comb = list(combinations(comb,3))
result = 0
count = 0

for com in comb:
    tmp = copy.deepcopy(adj)
    for c in com:
        tmp[c//m][c%m] = 1
    for v in vir:
        dfs(v//m,v%m)
    for tm in tmp:
        for t in tm:
            if t==0:
                count+=1
    result = max(count,result)
    count = 0
    visited = [[False] * m for _ in range(n)]
    tmp = []
print(result)



