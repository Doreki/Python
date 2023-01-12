n,m = map(int,input().split())
k = int(input())
left = 1
right = m
result = 0
for _ in range(k):
    des = int(input())
    if left <= des <= right:
        continue
    if des > right:
        value = des - right
        result+=value
        left +=value
        right +=value
    if des < left:
        value = left - des
        result +=value
        left -=value
        right -=value
print(result)