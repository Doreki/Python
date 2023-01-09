import collections
import sys

input = sys.stdin.readline

def bfs():
    global flag
    count = 0
    q = collections.deque()
    q.append(ji.pop())
    while q:
        for i in range(n):
            for j in range(m):
                print(a[i][j],end=" ")
            print()
        print()
        y,x = q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if a[y][x]=='J':
                if ny<0 or nx<0 or ny>=n or nx>=m:
                    q.clear()
                    result.append([y,x])
                    flag=True
                    break
                if a[ny][nx] == 'F' or visited1[ny][nx]==True or a[ny][nx] == '#':
                    count +=1
                    if count==4:
                        return
                    continue

                visited1[y][x] = True
                a[ny][nx] = 'J'
                num[ny][nx] = num[y][x]+1
                q.append([ny,nx])

        for i in range(n):
            for j in range(m):
                if a[i][j]=='F':
                    f.append([i,j])

        for fire in f:
            y,x = fire
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    continue
                if a[ny][nx] !='#':
                    a[ny][nx] = 'F'
        f.clear()
        count=0
n,m = map(int,input().split())

a = []
for _ in range(n):
  a.append(list(input()))

count = 0
dy = [0,-1,0,1]
dx = [1,0,-1,0]
ji = []
f = []
flag=False
result = []
num = [[0]*m for _ in range(n)]
visited1 = [[False]*m for _ in range(n)]
visited2 = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'J':
            ji.append([i,j])
bfs()
if flag:
    y,x = result.pop()
    print(num[y][x]+1)
else:
    print("IMPOSSIBLE")
