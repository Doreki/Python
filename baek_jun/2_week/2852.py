import sys
input = sys.stdin.readline

n = int(input())

lcount = 0
rcount = 0
pteam=""
lt=0
rt=0
for _ in range(n):
    team,time = input().split(" ")
    m,s = map(int, time.split(":"))
    time = m*60+s

    if lcount>rcount:
        lt += time-pt
    elif rcount>lcount:
        rt += time-pt

    if team=="1":
        lcount+=1
    elif team=="2":
        rcount+=1

    pteam = team
    pt = time
if lcount>rcount:
    lt += 48*60 - pt
elif rcount>lcount:
    rt += 48*60 - pt

print('{:0>2}:{:0>2}'.format(lt//60,lt%60))
print('{:0>2}:{:0>2}'.format(rt//60,rt%60))

