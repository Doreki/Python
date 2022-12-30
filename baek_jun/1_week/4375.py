while True:
    try:
        n = int(input())
    except:
        break
    a = 1
    count = 1
    while(True):
        if a%n ==0:
            break
        a = a*10+1
        count +=1
    print(count)
