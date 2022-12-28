cost = [0] + list(map(int,input().split()))
park = [0]*100
sum = 0
for _ in range(3):
    start,end = map(int,input().split())
    for i in range(start,end):
        park[i] += 1

for p in park :
    sum += cost[p]*p
print(sum)