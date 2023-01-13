while True:
    arr = list(map(int,input().split()))
    arr.sort()
    a,b,c = arr
    if a==0 and b==0 and c==0:
        break
    A = a**2+b**2
    B = c**2
    if A==B:
        print("right")
    else:
        print("wrong")
