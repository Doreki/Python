a,b = map(int,input().split())
str = ""

if(a%2==0) :
    str += "짝수+"
else :
    str += "홀수+"

if(b%2==0) :
    str += "짝수="
else :
    str += "홀수="

if((a+b)%2==0) :
    str += "짝수"
else :
    str += "홀수"

print(str)
