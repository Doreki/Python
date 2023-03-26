n = int(input())

arr = []
num = [1,2,3,4,5,6]

combi = list(combinations(num,3))

for i in range(n):
    arr.append(map(int,input().split()))

print(combi)



