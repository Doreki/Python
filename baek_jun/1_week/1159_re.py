n = int(input())
arr = []
alpha = [0]*26
for _ in range(n):
    arr.append(input())

for a in arr:
    al = a[0]
    alpha[ord(al) - ord('a')] +=1

result = ""
flag = False
for i in range(26):
    if alpha[i]>=5:
        result +=chr(i+ord('a'))
        flag = True
if flag:
    print(result)
else:
    print("PREDAJA")