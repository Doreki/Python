str = input()
result =""
for s in str:
    if s.isupper():
        num = ord(s) - ord('A')
        if num >= 13:
            result += chr(ord(s)-13)
        else:
            result += chr(ord(s)+13)
    elif s.islower():
        num = ord(s) - ord('a')
        if num >= 13:
            result += chr(ord(s) - 13)
        else:
            result += chr(ord(s) + 13)
    else:
        result+=s
print(result)