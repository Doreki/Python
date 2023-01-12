import collections

def bfs(a,b,c):
    q = collections.deque([[a,b,c]])
    v[a][b][c] = 1
    while q:
        a,b,c = q.popleft()
        if v[0][0][0]:
            break
        for at in attack:
            na = max(0,a - at[0])
            nb = max(0,b - at[1])
            nc = max(0,c - at[2])

            if v[na][nb][nc]:
                continue
            v[na][nb][nc] = v[a][b][c]+1
            q.append([na,nb,nc])
    return v[0][0][0] - 1

v = [[[0 for _ in range(64)] for _ in range(64)] for _ in range(64)]

attack = [
    [9,3,1],
    [9,1,3],
    [3,1,9],
    [3,9,1],
    [1,3,9],
    [1,9,3]
]

n = int(input())
arr = list(map(int,input().split()))
if len(arr) == 1:
    arr.append(0)
    arr.append(0)
if len(arr) == 2:
    arr.append(0)
# a,b,c = map(int,input().split())
print(bfs(arr[0],arr[1],arr[2]))