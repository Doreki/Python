def go(depth,start,length):
    if depth>n:
        return
    next=start+length//2
    ans[depth].append(a[next])

    go(depth+1,start,length//2)
    go(depth+1,next+1,length//2)

n = int(input())
a = list(map(int,input().split()))
ans = [[] for _ in range(n+1)]
go(1,0,len(a)-1)
for i in range(1,len(ans)):
    print(*ans[i])

