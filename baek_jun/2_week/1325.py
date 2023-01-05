import collections
import sys
input = sys.stdin.readline

def bfs(v):
    global count
    q = collections.deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        count +=1
        for i in node[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n,m = map(int,input().split())
node = [[] for _ in range(n+1)]
result = [0] * (n+1)
visited = [False] * (n+1)
count = 0
for _ in range(m):
    a,b = map(int,input().split())
    node[b].append(a)

for i in range(1,n+1):
    bfs(i)
    result[i] = count
    visited = [False] * (n + 1)
    count=0

max_num = max(result)
for i in range(len(result)):
    if result[i] == max_num:
        print(i,end=" ")
