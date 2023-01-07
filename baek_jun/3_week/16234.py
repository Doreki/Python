import sys
sys.setrecursionlimit(100000)

def is_union(y,x):

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >=n or nx >=n:
            continue
        diff = abs(adj[y][x] - adj[ny][nx])
        if l<= diff <=r:
            union[ny][nx] = True

def dfs(y,x):
    global count
    global sum
    if y < 0 or x < 0 or y >= n or x >= n or visited[y][x]==True or union[y][x]==False:
        return False

    if union[y][x]==True:
        visited[y][x] = True

        arr.append([y,x])
        sum+=adj[y][x]
        count+=1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            dfs(ny,nx)
        return True
    return False

n,l,r = map(int,input().split())

arr = []
adj = []
for _ in range(n):
    adj.append(list(map(int,input().split())))

dy = [0,-1,0,1]
dx = [1,0,-1,0]

union = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

sum = 0
count = 0
result = 0
flag = False
while True:

    for i in range(n):
        for j in range(n):
            is_union(i,j)

    for i in range(n):
        for j in range(n):
            if union[i][j] == True:
                flag = True

    if flag == False:
        break

    for i in range(n):
        for j in range(n):
            if dfs(i,j):
                avg = sum//count
                for a in arr:
                    y,x = a
                    adj[y][x] = avg
                arr = []
                count = 0
                sum =0

    visited = [[False] * n for _ in range(n)]

    union = [[False] * n for _ in range(n)]
    result +=1
    flag=False

print(result)
