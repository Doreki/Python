from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))
comb = list(combinations(arr, 7))
for c in comb :
    if sum(c)==100:
        cc = sorted(c)
        for c in cc :
            print(c)
        break