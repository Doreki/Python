import sys

sys.setrecursionlimit(100000)

def dfs(y,x,size):
    result = ""
    start = a[y][x]
    flag = True
    if size==1:
        return str(start)
    for i in range(y,y+size):
        for j in range(x,x+size):
            if a[i][j] != start:
                flag = False
                result += "("+ dfs(y,x,size//2)
                result += dfs(y,x+size//2,size//2)
                result += dfs(y+size//2,x,size//2)
                result += dfs(y+size//2,x+size//2,size//2)+")"
                return result
    return str(start)

n = int(input())
a = []
# result = ""
for _ in range(n):
    a.append(list(map(int,input())))

print(dfs(0,0,n))


