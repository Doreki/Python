str = input()
arr = [0]*26
for chr in str:
    arr[ord(chr) - ord('a')] += 1

for i in arr :
    print(i,end=" ")