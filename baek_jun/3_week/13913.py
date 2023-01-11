import collections


def bfs(n):
    q = collections.deque([n])
    visited[n] = 1
    a[n] = -1
    while q:
        now = q.popleft()
        arr = [now-1,now+1,now*2]
        for next in arr:
            if 0<= next <=100000:
                if not visited[next]:
                    q.append(next)
                    a[next] = now
                    visited[next] = visited[now]+1



a = [0]*100004
visited = [0]*100004
n,k = map(int,input().split())
bfs(n)

result = []
stack = []
stack.append(a[k])
result.append(k)
while stack:
    idx = stack.pop()
    if idx==-1:
        break
    result.append(idx)
    stack.append(a[idx])
result.reverse()
if n==k:
    print(0)
    print(n)
else:
    print(visited[k] - 1)
    print(*result)



