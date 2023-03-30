str = input()
arr = [0]*26

for s in str:
    arr[ord(s) - ord('a')] += 1

for a in arr:
    print(a,end=" ")