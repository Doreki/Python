import sys
input = sys.stdin.readline
def go(num) -> int:
    if num < 5:
        return 0
    return num//5+go(num//5)

n = int(input())
result = 0
for _ in range(n):
    num = int(input())
    print(go(num))
