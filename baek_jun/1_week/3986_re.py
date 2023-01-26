n = int(input())
count = 0
for _ in range(n):
    str = input()
    stack = []
    for s in str:
        if not stack:
            stack.append(s)
            continue
        if stack[-1] == s:
            stack.pop()
            continue
        else:stack.append(s)
    if stack:
        continue
    else:
        count +=1
print(count)