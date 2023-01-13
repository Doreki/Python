n,target = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = arr[i]+arr[j]+arr[k]
            if sum<=target:
                ans = max(ans,sum)
print(ans)