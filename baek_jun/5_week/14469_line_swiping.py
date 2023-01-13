import sys
input = sys.stdin.readline
n = int(input())

result = 0
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key= lambda x:x[0])
real_time = arr[0][0] + arr[0][1]
for i in range(1,n):
    real_time = max(real_time,arr[i][0])
    real_time += arr[i][1]
print(real_time)

