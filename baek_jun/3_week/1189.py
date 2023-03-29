import collections

n,m,k = map(int,input().split())

arr = [list(input()) for _ in range(n)]

startY = n-1
startX = 0
endY = 0
endX = m-1

visited = [[0] * m for _ in range(n)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]


def dfs(y,x):
    count = 0
    stack = []
    stack.append([y,x])

    while stack:
        y,x = stack.pop()
        count +=1
        visited[y][x]= count
        print(y,x)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or nx<0 or ny>=n or nx>=m or visited[ny][nx]:
                continue
            if arr[ny][nx] == 'T':
                continue
            stack.append([ny,nx])
            if ny==endY and nx==endX:
                count += 1
                visited[ny][nx] = count
                for i in visited:
                    for j in i:
                        print(j, end=" ")
                    print()
                print()
                return count



result = dfs(startY,startX)
print(result)
