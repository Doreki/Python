n,m = map(int,input().split())
numbers = list(map(int,input().split()))

sums = [0]*n
sum = 0
for i in range(m):
    sum += numbers[i]
sums[m-1] = sum

for i in range(m,n):
    sums[i] = sums[i-1]+numbers[i] - numbers[i-m]
print(max(sums[m-1:]))