n,m = map(int,input().split(" "))
location = [[0] * (m+1) for _ in range(n+1)]

for i in range(int(input())):
   l,d,x,y = map(int,input().split())
   if d==0:
       for i in range(y,y+l):
           location[x][i] = 1
   else:
       for i in range(x,x+l):
           location[i][y] = 1

for i in range(1,m+1):
    print()
    for j in range(1,n+1):
        print(location[i][j],end=" ")