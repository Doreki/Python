from itertools import combinations

n = int(input())

arr = []

num = []
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        num.append((i,j))

for i in range(n):
    arr.append(list(map(int,input().split())))


combi = list(combinations(num,3))
sum = 0

dy = [0,-1,0,1]
dx = [1,0,-1,0]
flag = False
count = 0
for comb in combi:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for c in comb:
        if flag:
            break
        y,x = c
        if visited[y][x]:
            break
        visited[y][x] = True
        for i in range(4):
            ny = dy[i]+y
            nx = dx[i]+x
            if ny <0 or nx<0 or ny>=n or nx>=n or visited[ny][nx]:
                flag = True
                break

            visited[ny][nx] = True



    if flag:
        continue

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count+=1
                sum += arr[i][j]



    if(count==15):
        result.append(sum)
    sum = 0
    count = 0

print(min(result))




