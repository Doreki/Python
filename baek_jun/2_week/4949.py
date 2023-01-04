while True:
    str = input()
    stack=[]

    flag=False
    if str==".":
        break
    for s in str:
        if s=="(" or s=="[":
            stack.append(s)
        elif s==")" or s=="]":
            if stack:
                p = stack.pop()
                if p=="(" and s=="]":
                    print("no")
                    flag = True
                    break
                elif p=="[" and s==")":
                    print("no")
                    flag = True
                    break
            else:
                print("no")
                flag = True
                break

    if flag==False:
        if stack:
            print("no")
        else:
            print("yes")
    flag=False
