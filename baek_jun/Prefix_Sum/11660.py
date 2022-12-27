import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [0]*(n+1)
sum = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

s = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        sum[i][j] = sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1] + graph[i-1][j-1]

for _ in range(m+1):
    x1,y1,x2,y2 = map(int,input().split())
    print(sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1])
