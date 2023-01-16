def good(x,y,op):
    if x<y and op=='<' :return True
    if x>y and op=='>' :return True
    return False

def go(idx,num):
    if idx == n+1:
        arr.append(num)
        return
    for i in range(10):
        if check[i]: continue
        if idx == 0 or good(num[idx - 1], str(i) + '0', a[idx-1]):
            check[i] = 1
            go(idx + 1,num + str(i))
            check[i] = 0
    return

n = input()
check = [0]*10
arr = []
a = ['']*20

for i in range(n):
    a[i] = i