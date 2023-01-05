from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

adj = []
house = []
chicken = []
dy = [0,-1,0,1]
dx = [1,0,-1,0]

visited = [[False] * n for _ in range(n)]
distance = [[0] * n for _ in range(n)]
for _ in range(n):
    adj.append(list(map(int,input().split())))

for i in range(len(adj)):
    for j in range(len(adj[i])):
        if adj[i][j] == 1:
            house.append([i,j])
        if adj[i][j] == 2:
            chicken.append([i,j])
comb = list(combinations(chicken,m))

arr = []
result = 0

min_num = 999999
sum = 0
for com in comb:
    for h in house:
        for c in com:
            y, x = h
            y1, x1 = c
            result = abs(y-y1)+abs(x-x1)
            min_num = min(result,min_num)
        sum += min_num
        result = 0
        min_num = 999999
    arr.append(sum)
    sum = 0
print(min(arr))