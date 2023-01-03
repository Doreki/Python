import collections

n,m = map(int,input().split())
arr = []
arr= list(map(int,input().split()))
dic = {}
count = 0
for a in arr:
    try:
        count = dic[a]
    except:
        dic[a] = 1
        count = 0
    dic[a] = count+1
dic = sorted(dic.items(),key= lambda x:-x[1])
for d in dic:
    for _ in range(d[1]):
        print(d[0],end=" ")