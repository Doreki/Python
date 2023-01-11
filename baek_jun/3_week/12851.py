import collections


def bfs(n):
    q = collections.deque([n])
    visited[n] = 1
    a[n] = 1
    while q:
        now = q.popleft()
        arr = [now-1,now+1,now*2]
        for next in arr:
            if 0<= next <=100000:
                if not visited[next] :
                    q.append(next)
                    visited[next] = visited[now]+1
                    a[next] += a[now]
                elif visited[next] == visited[now]+1:
                    a[next] += a[now]



a = [0]*100004
visited = [0]*100004
n,k = map(int,input().split())
count = 0
result = 0
bfs(n)
if n==k:
    print(0)
    print(1)
else :
    print(visited[k] - 1)
    print(a[k])


