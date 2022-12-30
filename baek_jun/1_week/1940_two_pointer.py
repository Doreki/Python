n = int(input())
target = int(input())
arr = list(map(int,input().split()))
left = 0
right = len(arr)-1
count = 0
arr.sort()
while(left<right):
    result = arr[left] + arr[right]
    if target == arr[left] + arr[right]:
        count +=1
        left += 1
    elif result > target :
        right -=1
    else:
        left +=1

print(count)