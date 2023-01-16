import sys
sys.setrecursionlimit(10000)
def dfs(y,x):
    if y<0 or x<0 or y>=n or x>=m or v[y][x]:
        return
    v[y][x] = True
    if a[y][x]==1:
        a[y][x]=0
        return
    dfs(y+1,x)
    dfs(y,x+1)
    dfs(y-1,x)
    dfs(y,x-1)
n,m = map(int,input().split())

a = []
v = [[False]* m for _ in range(n)]
count1 = 0
prev = 0
count2 = 0
for _ in range(n):
    a.append(list(map(int,input().split())))
while True:
    v = [[False] * m for _ in range(n)]
    flag = False
    prev = 0
    for i in a:
        for j in i:
            if j==1:
                flag=True
                prev +=1
    dfs(0,0)

    if not flag:
        break
    count1 +=1
    count2 = prev

print(count1)
print(count2)