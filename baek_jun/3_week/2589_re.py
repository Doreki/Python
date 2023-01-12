import collections

def bfs(y,x):
    q = collections.deque([[y,x]])
    max_num = 0
    if a[y][x] == 'W':
        return 0
    v[y][x] = 1
    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or ny>=n or nx>=m or v[ny][nx]:
                continue

            if a[ny][nx] == 'W':
                continue
            v[ny][nx] = v[y][x]+1
            max_num = max(v[ny][nx],max_num)
            q.append([ny,nx])
    return max_num
n,m = map(int,input().split())
a = []
v = [[0] * m for _ in range(n)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]
arr = []
for _ in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(m):
        arr.append(bfs(i,j))
        v = [[0] * m for _ in range(n)]

print(max(arr)-1)