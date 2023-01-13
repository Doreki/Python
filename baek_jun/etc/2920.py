arr = list(map(int,input().split()))

asc = sorted(arr)
desc = sorted(arr,reverse=True)

if arr==asc:
    print("ascending")
elif arr==desc:
    print("descending")
else:
    print("mixed")