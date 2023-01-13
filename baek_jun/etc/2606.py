def dfs(x):
    global count
    v[x]=True
    count +=1
    for i in arr[x]:
        if not v[i]:
            dfs(i)

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
result = []
v = [False]*(n+1)
count = 0
for _ in range(m):
    y,x = map(int,input().split())
    arr[y].append(x)
    arr[x].append(y)
dfs(1)
print(count-1)