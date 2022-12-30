import collections

str = input()
count = 0
counter = collections.Counter(str).most_common()
str1 = ""
str2 = ""
counter = sorted(counter,key=lambda x:x[0])
for c in counter :
    str1 += c[0] * (c[1]//2)
for c in counter :
    if c[1]%2==1 :
        str2 += c[0]
result = str1 + str2+ str1[::-1]
if result==result[::-1]:
    print(result)
else :
    print("I'm Sorry Hansoo")


