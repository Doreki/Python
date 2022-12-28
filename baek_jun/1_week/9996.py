n = int(input())
exp = input()
pre,suf = exp.split("*")
for _ in range(n):
    str = input()
    if str.find(pre) == 0:
        str = str[len(pre):]
        index = len(str) - len(suf)
        if index >= 0 and str.rfind(suf) == index:
            print("DA")
        else:
            print("NE")
    else :
        print("NE")
