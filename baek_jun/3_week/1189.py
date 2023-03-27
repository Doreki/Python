import collections

n,m,k = map(int,input().split())

arr = [list(input()) for _ in range(n)]

startY = n-1
startX = 0
endY = 0
endX = m-1

visited = [[False] * m for _ in range(n)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]


def bfs(y,x):
    count = 0
    visited[y][x] = True
    q = collections.deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or nx<0 or ny>=n or nx>=m or visited[ny][nx]:
                continue
            if arr[ny][nx] == 'T':
                continue
            if ny==endY and nx==endX:
                 count +=1
            visited[ny][nx] = True
            q.append([ny,nx])
    return count

result = bfs(startY,startX)
print(result)
