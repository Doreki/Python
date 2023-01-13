import sys
input = sys.stdin.readline
n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:x[0])
end = arr[0][0]+arr[0][1]
result = 0
for i in range(1,n):
    end = max(arr[i][0],end)
    end = end+arr[i][1]
print(end)