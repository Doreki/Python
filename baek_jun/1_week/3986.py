n = int(input())
count = 0
for _ in range(n):
    str = input()

    while "AA" in str or "BB" in str:
        str = str.replace("AA","")
        str = str.replace("BB","")
    if str == "":
        count +=1

print(count)