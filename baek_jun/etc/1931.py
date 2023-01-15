import sys
input = sys.stdin.readline
n = int(input())
arr = []
count = 0
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda x:(x[1],x[0]))
start = 0
end = 0
for a in arr:
    start = a[0]
    if end <= start:
        # 강의실 사용가능한 조건
        count +=1
        end = a[1]
print(count)