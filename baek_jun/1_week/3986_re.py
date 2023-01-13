n = int(input())
count = 0
for _ in range(n):
    stack = []
    arr = list(input())
    for a in arr:
        if stack and stack[-1]==a:
            stack.pop()
            continue
        stack.append(a)
    if not stack:
        count +=1
print(count)
