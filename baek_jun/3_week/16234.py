import collections


def bfs(y,x):
    global sum
    global count
    q = collections.deque([[y,x]])

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or ny>=n or nx>=n or v[ny][nx]:
                continue
            diff = abs(a[ny][nx] - a[y][x])
            if l<=diff<=r:
                q.append([ny,nx])
                arr.append([ny, nx])
                sum += a[ny][nx]
                v[ny][nx] = True
n,l,r = map(int,input().split())
dy = [0,-1,0,1]
dx = [1,0,-1,0]
a = []
v = [[False]* n for _ in range(n)]
sum = 0
result = 0
arr = []
flag = False
for _ in range(n):
    a.append(list(map(int,input().split())))

while True:
    v = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if v[i][j] ==False:
                arr.clear()
                v[i][j] = True
                arr.append([i,j])
                sum = a[i][j]
                bfs(i,j)
                if len(arr) ==1: continue
                for ar in arr:
                    y,x = ar
                    a[y][x] = sum//len(arr)
                    flag = True
    if not flag:
        break
    result +=1
print(result)