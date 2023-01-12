str = input()

alpa = [0]*26

for s in str:
    alpa[ord(s)- ord('a')] +=1

print(*alpa)