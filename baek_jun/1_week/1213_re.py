import collections

str = input()
str = list(str)
str.sort()
counter = collections.Counter(str)
count = 0
ans = ""
flag = False
odd=""
for c in counter.items():
    ch,num = c
    if num%2==1:
        count+=1
        ans += ch*((num-1)//2)
        odd=ch
    else:
        ans += ch*(num//2)
    if count>1:
        flag=True
        break
if not flag:
    print(ans+odd+ans[::-1])
else:
    print("I'm Sorry Hansoo")