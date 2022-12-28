cost = [0] + list(map(int,input().split()))
get_in = []
get_out = []
for _ in range(3):
    a,b = map(int,input().split())
    get_in.append(a)
    get_out.append(b)
start = min(get_in)
end = max(get_out)
count = 0
sum = 0
for i in range(start,end+1) :
    for j in get_in :
        if(i==j):
            count +=1
    for k in get_out :
        if(i==k):
            count -=1
    sum += count * cost[count]
print(sum)