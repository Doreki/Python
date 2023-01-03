n,m = map(int,input().split())
adj = []
for _ in range(n):
    adj.append(list(input()))
flag = False
count = 0
for i in range(n):
    for j in range(m):
        if adj[i][j] == 'c':
            flag = True
            count = 0
        if flag:
            adj[i][j] = count
            count +=1
        else:
            adj[i][j] = -1
    flag=False
    count = 0

for i in adj:
    for j in i:
        print(j,end=" ")
    print()
