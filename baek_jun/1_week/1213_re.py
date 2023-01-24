import collections

str = input()
arr = list(str)
arr.sort()
counter = collections.Counter(arr)
count = 0
ans = ""
cent = ""
flag = False
for c in counter.items():
    ch = c[0]
    num = c[1]
    if num%2 !=0:
        count+=1
        cent += ch
    if count>1:
        flag=True
    ans +=ch*(num//2)

if flag:
    print("I'm Sorry Hansoo")
else:
    print(ans+cent+ans[::-1])