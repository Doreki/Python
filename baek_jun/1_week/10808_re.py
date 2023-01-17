str = input()

alpha = [0] * 26

for s in str:
    alpha[ord(s) - ord('a')] +=1

print(*alpha)