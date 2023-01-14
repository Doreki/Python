n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = [0]*n
ans[0] = arr[0]
for i in range(1,n):
    ans[i] = arr[i]+ans[i-1]

print(sum(ans))