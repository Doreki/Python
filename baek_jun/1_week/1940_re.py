n = int(input())
target = int(input())
arr = list(map(int,input().split()))
left = 0
right = n-1
count = 0
arr.sort()

while left<right:
    sum = arr[left]+arr[right]
    if sum==target:
        count +=1
        left +=1
    elif sum < target:
        left +=1
    else:
        right -=1
print(count)