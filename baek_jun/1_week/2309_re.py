import itertools

arr = []
for _ in range(9):
    arr.append(int(input()))

comb = list(itertools.combinations(arr,7))
ans = []
for c in comb:
    if sum(c) == 100:
        ans = list(c)
ans.sort()
for a in ans:
    print(a)