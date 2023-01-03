n,m = map(int,input().split())
t = int(input())
result = 0
next = 0
here = 1
sum = 0
length = m-1
for _ in range(t):
    next = int(input())
    if here > next:
        result = here - next
        here = next
    elif next > here+length:
        result = next- here -length
        here = next - length
    else : continue
    sum += result
print(sum)