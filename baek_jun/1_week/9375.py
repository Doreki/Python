import collections

t = int(input())
for _ in range(t) :
    n = int(input())
    arr = []
    sum = 1
    for _ in range(n):
        _,category = input().split()
        arr.append(category)
    counter = collections.Counter(arr)
    for c in counter.values():
        sum *= c+1
    print(sum-1)

