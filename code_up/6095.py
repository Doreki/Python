n = int(input())

baduk = [[0]* 19 for _ in range(19)]
for i in range(n) :
    x,y = map(int,input().split())
    baduk[x][y] = 1

for i in range(19) :
    print()
    for j in range(19) :
        print(baduk[i][j],end=" ")

