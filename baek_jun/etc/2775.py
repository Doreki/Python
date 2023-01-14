t = int(input())
d = [[0]*15 for _ in range(15)]
for i in range(1,15):
    d[0][i] = i

for _ in range(t):
    y = int(input())
    x = int(input())
    for i in range(1,y+1):
        for j in range(1,x+1):
            d[i][j] = d[i][j-1]+d[i-1][j]
    print(d[y][x])