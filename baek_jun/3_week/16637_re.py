import collections


def op(num1,num2,exp):
    if exp=='+':
        return num1+num2
    elif exp=='*':
        return num1*num2
    elif exp=='-':
        return num1-num2

def go(idx,_num):
    global result
    if idx == len(num)-1:
        result = max(result,_num)
        return
    go(idx+1,op(_num,num[idx+1],exp[idx]))
    if idx+2 <=len(num)-1:
        tmp = op(num[idx+1],num[idx+2],exp[idx+1])
        go(idx+2,op(_num,tmp,exp[idx]))



n = int(input())

arr = input()
num = []
exp = []
result = -123456789
for a in arr:
    if a.isdigit():
       num.append(int(a))
    else:
        exp.append(a)
go(0,num[0])

print(result)
