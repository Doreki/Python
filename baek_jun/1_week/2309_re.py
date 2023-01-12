arr = []
for _ in range(9):
    arr.append(int(input()))

num = sum(arr) - 100
result = []
for i in range(9):
    for j in range(9):
        if arr[i]+arr[j]==num:
            result = [i,j]

x,y = result
del arr[x],arr[y]
arr.sort()
for a in arr:
    print(a)
