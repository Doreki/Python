n = int(input())
target = int(input())
arr = list(map(int,input().split()))
arr.sort()
left = 0
right = n-1
sum = 0
count = 0
while left!=right:
    sum = arr[left]+arr[right]
    if sum==target:
        count+=1
        left+=1
    elif sum>target:
        right -=1
    else:
        left +=1

print(count)