n,m = map(int,input().split())
a = []
for _ in range(n):
  a.append(list(input()))

prev=-1
for i in range(n):
    for j in range(m):
        if a[i][j] !='c':
            a[i][j] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'c':
            a[i][j] = 0
            prev=0
            continue
        if prev>=0:
            a[i][j] = prev+1
        prev = a[i][j]
    prev=-1

for i in a:
    for j in i:
        print(j,end=" ")
    print()
