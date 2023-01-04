n = int(input())

stack = []
for _ in range(n):
    exp = input()
    try:
        for e in exp:
            if e=="(":
                stack.append(e)
            else:
                stack.pop()
        if stack:
            print("NO")
        else:
            print("YES")
        stack = []
    except:
        print("NO")
