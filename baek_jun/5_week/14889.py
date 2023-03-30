from itertools import combinations


n = int(input())
num = []
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    num.append(i)

comb = list(combinations(num,n//2))
tmp = []
result = []
sum1 = 0
sum2 = 0
for i in range(len(comb)//2):
    filtered = [x for x in num if x not in comb[i]]
    tmp1 = list(combinations(comb[i],2))
    tmp2 = list(combinations(filtered,2))
    for j in range(len(tmp1)):
        y,x = tmp1[j]
        ny,nx = tmp2[j]
        sum1 += arr[y][x]+arr[x][y]
        sum2 += arr[ny][nx]+arr[nx][ny]
    result.append(abs(sum1-sum2))
    sum1 = 0
    sum2 = 0

print(min(result))


