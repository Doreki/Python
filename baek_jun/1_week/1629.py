def mul(a,b):
    if(b==1):
        return a%c
    num = mul(a, b // 2)
    num = (num*num) % c
    if(b%2): num = (num * a) % c
    return num

a,b,c = map(int,input().split())
print(mul(a,b)%c)