n,k = map(int,input().split())
num = list(map(int,input().split()))
ans = sum(num[0:k])
arr = []
arr.append(ans)
for i in range(k,n):
    ans = ans+num[i] - num[i-k]
    arr.append(ans)
print(max(arr))
