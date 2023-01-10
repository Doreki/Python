def preorder(here):
    count = 0
    child = 0
    global num
    for t in tree[here]:
        if t == num:
            continue
        count +=preorder(t)
        child +=1
    if child ==0 : return 1
    return count

n = int(input())
visited = [False]*n
tree = [[] for _ in range(n)]
arr = list(map(int,input().split()))
root = 0
count = 0
for i in range(len(arr)):
    if arr[i] == -1:
        root = i
        continue
    tree[arr[i]].append(i)
num = int(input())
if num == root:
    print(0)
else:
    print(preorder(root))
