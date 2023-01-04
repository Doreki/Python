n = int(input())
num=666
count = 1
while True:
    if count == n:
        break
    num+=1
    ss = str(num)
    if ss.find("666") !=-1:
        count+=1
    num = int(ss)
print(num)