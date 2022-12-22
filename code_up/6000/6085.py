import math

w,h,b = input().split(" ")
w = int(w)
h = int(h)
b = int(b)

mb = w*h*b/(8*1024*1024)
mb = round(mb,2)
print(format(mb,".2f"),"MB", sep=" ")