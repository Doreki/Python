import collections


def bfs(y,x):
    global q
    global tmp
    q = collections.deque([[y, x]])
    tmp = collections.deque()
    global flag
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or nx<0 or ny>=n or nx>=m or v[ny][nx]:
                continue
            v[ny][nx] = count
            if a[ny][nx] != '0':
                a[ny][nx] = '0'
                tmp.append([ny,nx])
            else:
                q.append([ny,nx])
    q=tmp


n,m = map(int,input().split())
y1,x1,y2,x2 = map(int,input().split())
v = [[0]*m for _ in range(n)]
a = []
dy = [0,-1,0,1]
dx = [1,0,-1,0]

flag = False
count = 0
for _ in range(n):
    a.append(list(input()))
v[y1-1][x1-1] = 1
q = collections.deque([[y1-1, x1-1]])
while a[y2-1][x2-1] != '0':

    count+=1
    tmp = collections.deque()
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m or v[ny][nx]:
                continue
            v[ny][nx] = count
            if a[ny][nx] != '0':
                a[ny][nx] = '0'
                tmp.append([ny, nx])
            else:
                q.append([ny, nx])
    q = tmp
    for i in v:
        for j in i:
            print(j,end=" ")
        print()
    print()


print(v[y2-1][x2-1])