a,r,n = input().split()
a = int(a)
r = int(r)
n = int(n)

for i in range(2,n+1):
    a *= r

print(a)