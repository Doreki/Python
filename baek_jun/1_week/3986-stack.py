n = int(input())
count = 0
for _ in range(n):
    str = input()
    stack = []
    for s in str:
        if(len(stack) and stack[-1]==s):
            stack.pop()
        else :stack.append(s)
    if len(stack) == 0:
        count +=1
print(count)