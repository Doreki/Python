a,b,c = map(int,input().split())
arr = [0]*100
for _ in range(3):
    start,end = map(int,input().split())
    for i in range(start,end):
        arr[i] +=1

result = 0
for ar in arr:
    if ar==1:
        result+=a
    if ar==2:
        result+=2*b
    if ar==3:
        result+=3*c
print(result)