n = int(input())
target = int(input())
arr = list(map(int,input().split()))
targets = [0]*n
count = 0

for i in range(len(arr)):
    targets[i] = target - arr[i]

for i in range(len(targets)-1):
    if targets[i] in arr[i+1:]:
        count +=1
print(count)