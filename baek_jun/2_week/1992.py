import sys

sys.setrecursionlimit(100000)

def dfs(y,x,size):
    flag = False
    result = ""
    if size==1: return str(adj[y][x])
    for i in range(y,y+size):
        for j in range(x,x+size):
            num = adj[y][x]
            if num != adj[i][j]:
                result += "("
                result +=dfs(y,x,size//2)
                result +=dfs(y,x+size//2,size//2)
                result +=dfs(y+size//2,x,size//2)
                result +=dfs(y+size//2,x+size//2,size//2)
                result +=")"
                return result
    return str(adj[y][x])

n = int(input())
result =""
adj = []

for _ in range(n):
    adj.append(list(map(int,input())))
result = dfs(0,0,n)
print(result)

