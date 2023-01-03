def isPassable(str):
    flag=False
    isMo=False
    current=""
    count=0
    for s in str:
        if s == current and (s != 'e' and s != 'o'):
            return False
        if isMo==(s in mo):
            count +=1
        else:
            count = 1
        if s in mo:
            flag = True
            isMo = True
        else:
            isMo = False
        current = s
        if count >=3:
            return False

    if flag is False:
        return False
    return True

mo = ['a','e','i','o','u']
while True:
    str = input()
    if str == "end": break
    if(isPassable(str)):
        print(f'<{str}> is acceptable.')
    else:
        print(f'<{str}> is not acceptable.')
