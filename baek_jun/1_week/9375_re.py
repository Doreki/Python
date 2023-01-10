import collections

n = int(input())

for _ in range(n):
    number = int(input())
    arr = []
    result = 1
    for _ in range(number):
        _,category = input().split()
        arr.append(category)
    counter = collections.Counter(arr)
    for c in counter.items():
        result *= c[1]+1
    print(result-1)
