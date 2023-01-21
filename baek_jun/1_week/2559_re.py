n,k = map(int,input().split())

num = list(map(int,input().split()))
ans = [0]*(n-k+1)

ans[0] = sum(num[0:k])
for i in range(k,len(num)):
    ans[i-k+1] = ans[i-k] + num[i] - num[i-k]
print(max(ans))