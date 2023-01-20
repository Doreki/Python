str = input()
ans = ""

for s in str:
    if not s.isalpha():
        ans +=s
    else:
        if s.isupper():
            num = ord(s) - ord('A')
            if num >= 13:
                num = num - 13 + ord('A')
                ans +=chr(num)
            else:
                num = num + 13 + ord('A')
                ans +=chr(num)
        elif s.islower():
            num = ord(s) - ord('a')
            if num >= 13:
                num = num - 13 + ord('a')
                ans += chr(num)
            else:
                num = num + 13 + ord('a')
                ans += chr(num)
print(ans)

