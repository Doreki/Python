import collections

n,k = map(int,input().split())
arr = list(map(int,input().split()))
dic = {}
for a in arr:
    try:
        dic[a] +=1
    except:
        dic[a] = 1
dic = sorted(dic.items(),key= lambda x:-x[1])
for d in dic:
    for i in range(d[1]):
        print(d[0],end=" ")