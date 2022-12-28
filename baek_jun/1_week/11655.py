str = input()
result = ""
for s in str :
    if 65<= ord(s) <= 90 :
        if 90 < ord(s) + 13 :
            result += chr(ord(s) - 13)
        else :
            result += chr(ord(s) + 13)
    elif 97<= ord(s) <= 122 :
        if 122 < ord(s) + 13 :
            result += chr(ord(s) - 13)
        else :
            result += chr(ord(s) + 13)
    else :
        result += s
print(result)