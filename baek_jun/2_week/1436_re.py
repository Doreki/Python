n = int(input())
num = 666
count = 0
while  True:
    num = str(num)
    if num.find('666') == -1:
        num = int(num) + 1
    else:
        count += 1
        if count==n:
            break
        num = int(num) + 1


print(num)
