import sys
input = sys.stdin.readline

n,m = map(int,input().split())
poke = {}
number = {}
for i in range(n):
    p = input().rstrip()
    poke[p] = i+1
    number[str(i+1)] = p
for _ in range(m):
    str = input().rstrip()
    if 65<=ord(str[0])<=90 or 65<=ord(str[len(str)-1])<=90: #문자일때
        print(poke[str])
    else :
        print(number[str])

