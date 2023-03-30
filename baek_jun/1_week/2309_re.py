from itertools import combinations

arr = []

for _ in range(9):
    arr.append(int(input()))

combi = list(combinations(arr, 7))

for comb in combi:
    if sum(comb) == 100:
        comb = list(comb)
        break
comb.sort()
for com in comb:
    print(com)