import sys
input = sys.stdin.readline

n = int(input())
name = []
alpha = [0]*26
result = []
for _ in range(n):
    name.append(input())

for n in name:
    alpha[ord(n[0]) - ord('a')] +=1

flag = False
for i in range(26):
    if alpha[i] >= 5:
        s = chr(i + ord('a'))
        print(s,end="")
        flag=True

if not flag:
    print("PREDAJA")

