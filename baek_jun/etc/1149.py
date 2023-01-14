import sys
input = sys.stdin.readline
n = int(input())
r = []
g = []
b = []
dp = [[0]*3 for _ in range(n)]
for _ in range(n):
    a,bb,c = map(int,input().split())
    r.append(a)
    g.append(bb)
    b.append(c)
dp[0][0] = r[0]
dp[0][1] = g[0]
dp[0][2] = b[0]
for i in range(1,n):
    dp[i][0] = r[i]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = g[i]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = b[i]+min(dp[i-1][0],dp[i-1][1])
print(min(dp[i]))
