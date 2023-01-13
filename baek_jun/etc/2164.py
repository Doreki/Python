import collections

n = int(input())
q = collections.deque()
for i in range(1,n+1):
    q.append(i)
while True:
    if len(q)==1:
        break
    q.popleft()
    top = q.popleft()
    q.append(top)
print(q.pop())