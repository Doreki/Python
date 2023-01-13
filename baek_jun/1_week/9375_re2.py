import collections

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    result = 1
    for _ in range(n):
        _,cate = input().split()
        arr.append(cate)
    counter = collections.Counter(arr)
    for c in counter.values():
        result *= c+1
    print(result-1)