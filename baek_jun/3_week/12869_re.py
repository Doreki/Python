import collections
def solve(a,b,c) :
    visited[a][b][c] = 1
    q.append([a,b,c])
    while q:
        a,b,c = q.popleft()
        q.popleft()
        if visited[0][0][0]: break
        for i in range(6):
            na = max(0, a - _a[i][0])
            nb = max(0, b - _a[i][1])
            nc = max(0, c - _a[i][2])
            if visited[na][nb][nc] : continue
            visited[na][nb][nc] = visited[a][b][c] +1
            q.append([na,nb,nc])
    return visited[0][0][0] - 1
dp = [[[0 for _ in range(64)] for _ in range(64)] for _ in range(64)]
visited = [[[0 for _ in range(64)] for _ in range(64)] for _ in range(64)]
_a = [
    [9,3,1],
    [9,1,3],
    [3,1,9],
    [3,9,1],
    [1,3,9],
    [1,9,3]
]
q = collections.deque()
n = int(input())
a = []
a = list(map(int,input().split))
print(solve(a[0],a[1],a[2]))
