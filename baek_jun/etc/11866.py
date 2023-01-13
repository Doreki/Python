import collections

n,k = map(int,input().split())
q = collections.deque()
for i in range(1,n+1):
    q.append(i)
arr = []
while q:
    for i in range (1,k+1):
        first = q.popleft()
        if i==k:
            arr.append(first)
        else:
            q.append(first)
print("<",end="")
for i in range(n):
    if i==n-1:
        print(str(arr[i]),end="")
    else:print(str(arr[i])+",",end=" ")
print(">",end="")