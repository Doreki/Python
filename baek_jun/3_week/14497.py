import collections


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
            visited[ny][nx] = True
            if a[ny][nx] == '1':
                a[ny][nx] = '0'
                continue
            if ny == y2-1 and nx == x2-1:
                flag=True
                break
            q.append([ny,nx])

n,m = map(int,input().split())
y1,x1,y2,x2 = map(int,input().split())
a = []
dy = [0,-1,0,1]
dx = [1,0,-1,0]
flag = False
visited = [[False]*(m) for _ in range(n)]
for _ in range(n):
    a.append(list(input()))
count = 0
while True:
    bfs(y1-1,x1-1)
    count +=1
    visited = [[False] * (m) for _ in range(n)]
    if flag:
        break
print(count)
