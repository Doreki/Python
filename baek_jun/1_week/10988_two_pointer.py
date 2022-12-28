str = input()
left = 0
right = len(str) - 1
count = 0

while left <= right :
    if(str[left] is not str[right]) :
        count += 1
        print(0)
        break
    left +=1
    right -=1
if count == 0 :print(1)