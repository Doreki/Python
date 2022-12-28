n = int(input())
players = []
cnt = [0]*26
count = 0
for _ in range(n):
    players.append(input())

for player in players :
    a = ord(player[0]) - ord('a')
    cnt[a] +=1

for i in range(len(cnt)) :
    if cnt[i]>=5 :
        print(chr(i+ord('a')),end="")
        count +=1

if count == 0 : print("PREDAJA")