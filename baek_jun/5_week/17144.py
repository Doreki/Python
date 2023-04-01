import copy

n,m,k = map(int,input().split())

arr = []
tmp = []
for _ in range(n):
    arr.append(list(map(int,input().split())))


dy = [0,-1,0,1]
dx = [1,0,-1,0]
count = 0
start = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            start.append(i)
            start.append(j)
            break

for _ in range(k):
    tmp = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            count = 0
            for k in range(4):
                ny = dy[k]+i
                nx = dx[k]+j
                if tmp[i][j] <= 0:
                    break
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                if tmp[ny][nx] == -1:
                    continue
                arr[ny][nx] += tmp[i][j]//5
                # print(tmp[i][j]//5,arr[ny][nx])
                count +=1
            arr[i][j] -= (tmp[i][j]//5)*count

    tmp = copy.deepcopy(arr)
    y2,x2 = start[0],start[1]
    y1,x1 = y2+1,x2
    ny,nx = 0,0

    oy,ox = y1,x1

    while True:

        if oy == y1 and ox != m-1:
            ny,nx = oy,ox+1
        elif ox == m-1 and oy != n-1:
            ny,nx = oy+1,ox
        elif oy == n-1 and ox != 0:
            ny,nx = oy,ox-1
        elif ox == 0 and oy != y1:
             ny,nx = oy-1,ox
             if ny == y1 and nx == x1:
                 break

        arr[ny][nx] = tmp[oy][ox]
        if tmp[oy][ox] == -1:
            arr[ny][nx] = 0
        if tmp[ny][nx] == -1:
            arr[ny][nx] = -1
        oy,ox = ny,nx

    ny,nx=0,0
    oy,ox = y2,x2
    while True:

        if oy == y2 and ox != m-1:
            ny,nx = oy,ox+1
        elif ox == m-1 and oy != 0:
            ny,nx = oy-1,ox
        elif oy == 0 and ox != 0:
            ny,nx = oy,ox-1
        elif ox == 0 and oy != y2:
             ny,nx = oy+1,ox
             if ny == y2 and nx == x2:
                 break

        arr[ny][nx] = tmp[oy][ox]
        if tmp[oy][ox] == -1:
            arr[ny][nx] = 0
        if tmp[ny][nx] == -1:
            arr[ny][nx] = -1
        oy,ox = ny,nx
sum = 0
for a in arr:
    for j in a:
        if j==-1:
            continue
        sum+=j

print(sum)



