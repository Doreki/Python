import collections

n = int(input())

arr = [[0] * n for _ in range(n)]

a = int(input())

for _ in range(a):
    y,x = list(map(int,input().split()))
    arr[y-1][x-1] = 1

l = int(input())

dArr = collections.deque()

for _ in range(l):
    dArr.append(list(input().split()))

q = collections.deque()

dy = [0,1,0,-1]
dx = [1,0,-1,0]

sec = 0
next = dArr.popleft()

q.append((0,0))
dr = 0
count = 0
while True:
    count +=1
    sec +=1
    y,x = q[-1]
    dsec,dd = next


    if dr < 0:
        dr = 3
    elif dr>=4:
        dr = 0

    ny = y+dy[dr]
    nx = x+dx[dr]
    if ny<0 or nx<0 or ny>=n or nx>=n:
        break
    if (ny,nx) in q:
        break
    if arr[ny][nx] == 1:
        arr[ny][nx] = 0
        q.append((ny,nx))
    else:
        q.popleft()
        q.append((ny,nx))
    if int(dsec)==sec:
        if dArr:
            next = dArr.popleft()
        if dd=='D':
            dr +=1
        elif dd=='L':
            dr -=1

print(count)