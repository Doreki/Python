n = int(input())
exp = []
for _ in range(n):
    flag = False
    exp = list(input())
    stack = []
    try:
        for e in exp:

            if e =='(':
                stack.append(e)
            elif e ==')':
                stack.pop()

    except:
            flag = True
    if stack or flag:
        print('NO')
    else:
        print('YES')