mo = ['a','e','i','o','u']
count = 0
prev = ""
while True:
    flag=False
    str = input()
    moo = 0
    ja = 0
    if str=="end":
        break
    for s in str:
        if s in mo:
            flag=True
    for s in str:
        if s in mo:
            moo+=1
            ja=0
        else:
            ja+=1
            moo=0
        if moo==3 or ja==3:
            flag=False
    for s in str:
        if prev==s:
            if s!="e" or s!="o":
                flag=False
        prev=s

    if flag:
        print(f"<{str}> is acceptable")
    else:
        print(f"<{str}> is not acceptable")

