price = list(map(int,input().split()))
arr = [0]*104
for _ in range(3):
    start,end = map(int,input().split())
    for i in range(start,end):
        arr[i] +=1
result = 0
for a in arr:
    if a==1:
        result +=price[0]
    if a==2:
        result +=price[1]*2
    if a==3:
        result +=price[2]*3
print(result)