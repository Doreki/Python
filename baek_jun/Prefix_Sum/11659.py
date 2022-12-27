import sys
input = sys.stdin.readline

n,m = map(int,input().split())
numbers = [0]+list(map(int,input().split()))
sum = [0]*(n+1)
tmp = 0

for i in range(1,n+1):
    sum[i] = sum[i-1]+numbers[i]
for _ in range(m) :
    x,y = map(int,input().split())
    print(sum[y]-sum[x-1])