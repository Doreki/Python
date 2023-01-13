n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr = set(arr)
arr = list(arr)
arr.sort(key=lambda x:(len(x),x))
for a in arr:
    print(a)