import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
def dfs(y,x):
    if y<0 or x<0 or y>=n or x>=m:
        return False
    if v[y][x]:
        return False
    if a[y][x] ==1:
        v[y][x] = True
        dfs(y+1,x)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y,x-1)
        return True
    return False


t = int(input())
for _ in range(t):
    count = 0
    m,n,k = map(int,input().split())
    a = [[0] * m for _ in range(n)]
    v = [[False] * m for _ in range(n)]
    for _ in range(k):
        i,j = map(int,input().split())
        a[j][i] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                count+=1
    print(count)
