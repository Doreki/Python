import collections
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    ans = 1
    for _ in range(n):
        _,cate = input().split()
        arr.append(cate)
    counter = collections.Counter(arr)

    for c in counter.values():
        ans *= c+1

    print(ans-1)