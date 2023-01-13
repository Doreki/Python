import sys
input = sys.stdin.readline
n = int(input())

result = 0
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key= lambda x:x[0])
for i in range(n):
    next,time = arr[i]

    if result >= next:
        result+= time
    else :
        result = next+time
print(result)

