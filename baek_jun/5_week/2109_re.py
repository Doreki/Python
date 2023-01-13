import heapq
n = int(input())
arr = []
result = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[1])
for a in arr:
    heapq.heappush(result,a[0])
    if len(result)> a[1]:
        heapq.heappop(result)
print(sum(result))