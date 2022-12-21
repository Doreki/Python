n = int(input())
list = input().split()
for i in range(n):
    list[i] = int(list[i])
d = []
for i in range(n-1,-1,-1):
    print(list[i],end=" ")