import sys
input = sys.stdin.readline

n = int(input())

score_1 = 0
score_2 = 0
t_1 = 0
t_2 = 0
prev_time = 0
prev_team = ""
for _ in range(n):
    score,t = input().split()
    m,s = map(int,t.split(":"))
    t = m*60+s


    if score_1>score_2:
        t_1 += t - prev_time
    elif score_2>score_1:
        t_2 += t - prev_time

    if score=='1':
        score_1+=1
    else:
        score_2+=1
    prev_time = t
if score_1 > score_2:
    t_1 += 48*60 - prev_time
if score_2 > score_1:
    t_2 += 48*60 - prev_time

print('{:0>2}:{:0>2}'.format(t_1//60,t_1%60))
print('{:0>2}:{:0>2}'.format(t_2//60,t_2%60))
