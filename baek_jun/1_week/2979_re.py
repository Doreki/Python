price = [0]+list(map(int,input().split()))



arr = [0]*100
result = 0
for i in range(3):
    start,end = map(int,input().split())
    for j in range(start,end):
        arr[j] +=1

for a in arr:
    result += price[a]*a

print(result)