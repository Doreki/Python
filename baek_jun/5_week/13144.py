import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
cnt = [0] * 100004
result = 0
sum = 0
r = -1

for l in range(n):
    while r+1 < n and cnt[arr[r+1]] == 0:
        r+=1
        cnt[arr[r]] +=1
        sum +=1
    result +=sum
    sum -=1
    cnt[arr[l]] -=1

print(result)