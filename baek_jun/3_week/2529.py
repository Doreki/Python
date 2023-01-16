def go(num):
    global flag
    while True:
        for i in range(n+1):
            if i == n:
                flag = True
                break
            if exp[i] == '<':
                if num[i] < num[i+1]:
                    continue
                else:
                    num[i],num[i+1] = num[i+1],num[i]
                    break
            elif exp[i] == '>':
                if num[i] > num[i+1]:
                    continue
                else:
                    num[i],num[i+1] = num[i+1],num[i]
                    break

        if flag:
            return
n = int(input())
exp = list(input().split())
num1 = []
num2 = []
flag = False
for i in range(n+1):
    num1.append(i)
for i in range(9,8-n,-1):
    num2.append(i)

go(num1)
flag=False
go(num1)
flag=False
go(num2)
ans1=""
ans2=""
for i in range(n+1):
    ans1+=str(num1[i])
    ans2+=str(num2[i])
print(ans2)
print(ans1)
