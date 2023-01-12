from itertools import combinations

n,k = map(int,input().split())

a = []
chi = []
hou = []
dis = 0
min_num = 987654321
result = 0
arr = []
for _ in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if a[i][j] == 2 :
            chi.append([i,j])
        if a[i][j] == 1 :
            hou.append([i,j])

comb = list(combinations(chi,k))
for com in comb:
    for h in hou:
        for c in com:
            y1,x1 = h
            y2,x2 = c
            dis = abs(y1-y2) + abs(x1-x2)
            min_num = min(min_num,dis)
        result+=min_num
        min_num = 987654321
    arr.append(result)
    result = 0
print(min(arr))