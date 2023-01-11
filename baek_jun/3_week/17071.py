import collections


def bfs(n):
    q = collections.deque([n])
    visited[n] = True
    a[n] = 1
    max_num = 0
    global k
    global flag
    while q:
        now = q.popleft()
        if now==k:
            break
        arr = [now-1,now+1,now*2]
        if a[now] > max_num:
            k += a[now]-1
            max_num = a[now]

        if k>500000:
            flag=True
            return
        for next in arr:
            bro = k + a[now]
            if 0<= next <=1000000:
                if bro==next:
                    a[next] = a[now]+1
                    if a[next]:
                        visited[next] = False #동생이 있는 위치가 이미 방문했다면 풀어준다.
                if not visited[next] :
                    q.append(next)
                    visited[next] = True
                    # if not a[next] : #할당이 안되어 있으면
                    a[next] = a[now]+1


visited = [0]*1000004
a = [0]*1000004
n,k = map(int,input().split())
tmp = n
count = 0
result = 0
flag = False
bfs(n)
if n==k:
    print(0)
elif flag:
    print(-1)
else :
    print(a[k]-1)


