import collections
import sys

input = sys.stdin.readline

def bfs(y,x):
    visited[y][x] = True
    global flag
    q = collections.deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or nx<0 or ny>=n or nx>=m or visited[ny][nx]:
                continue
            if a[ny][nx] == 'X':
                continue
            if a[ny][nx] == 'L':
                flag=True
                break
            visited[ny][nx] = True
            q.append([ny,nx])

def go(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if a[ny][nx] == 'X':
            a[ny][nx] = '.'

n,m = map(int,input().split())
a = []
count = 0
dy = [0,-1,0,1]
dx = [1,0,-1,0]
visited = [[False]*(m) for _ in range(n)]
flag = False
for _ in range(n):
    a.append(list(input()))

water = []
L = []


while True:
    for i in range(n):
        for j in range(m):
            if a[i][j] =='.'or a[i][j] == 'L':
                water.append([i,j])
            if a[i][j] =='L':
                L.append([i,j])
    for w in water:
        y,x = w
        go(y,x)
    y,x = L[0]
    bfs(y,x)
    count+=1
    visited = [[False]*(m) for _ in range(n)]
    water = []
    L = []
    if flag:
        break
print(count)
