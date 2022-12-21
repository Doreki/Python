n = int(input())
list = input().split()

for i in range(n):
    list[i] = int(list[i])

list.sort()

print(list[0])