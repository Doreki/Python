h,b,c,s = input().split(" ")
h = int(h)
b = int(b)
c = int(c)
s = int(s)

mb = h * b * c * s/(8*1024*1024)

print(round(mb,1),"MB",sep=" ")