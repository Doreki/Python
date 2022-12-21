n = int(input())
list = input().split()
for i in range(n):
    list[i] = int(list[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[list[i]] +=1

for i in range(1,24):
    print(d[i],end=" ")