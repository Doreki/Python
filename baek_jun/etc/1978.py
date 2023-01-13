n = int(input())
arr = list(map(int,input().split()))
ans = 0
count = 0
for a in arr:
    for i in range(2,a+1):
        if a%i==0:
            count+=1
    if count==1:
        ans +=1
    count=0
print(ans)