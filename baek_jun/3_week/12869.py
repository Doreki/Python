import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])
p_q = []
for a in arr:
    print(a[0],p_q)
    heapq.heappush(p_q, a[0])
    if (len(p_q)>a[1]):
        print(a[0],p_q)
        heapq.heappop(p_q)

print(sum(p_q))