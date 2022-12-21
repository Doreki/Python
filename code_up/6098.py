location = [[0] * 11 for _ in range(11)]

for i in range(10) :
  a=input().split()
  for j in range(10) :
    location[i+1][j+1]=int(a[j])


    x = 2
    y = 2
    location[x][y] = 9
while(True):
    if location[x][y+1] == 2:
        y +=1
        location[x][y] = 9
        break
    elif location[x][y+1] == 0:
        y +=1
        location[x][y] = 9
    else:
        if location[x+1][y] == 2:
            x +=1
            location[x][y] = 9
            break
        elif location[x + 1][y] == 0:
            x += 1
            location[x][y] = 9
        else :
            break

for i in range(1,11):
    for j in range(1,11):
        print(location[i][j],end=" ")
    print()