n = int(input())
arr = []
num = ""
flag = False
for _ in range(n):
    str = input()
    for i in range(len(str)):
        if str[i].isdigit():
            flag=True
        else:
            flag=False

        try:
            if flag:
                num+=str[i]
            else:
                arr.append(int(num))
                num=""
            if i==len(str)-1:
                arr.append(int(num))
                num=""
        except:
            pass
arr.sort()

for a in arr:
    print(a)
