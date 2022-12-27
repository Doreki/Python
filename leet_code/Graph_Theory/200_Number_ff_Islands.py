class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if self.bfs(grid,i,j) == True:
                    count += 1

        return count

    def bfs(self,grid,x,y) :

        if x <= -1 or x >= len(grid) or y <= -1 or y >= len(grid[0]):
            return False
        if grid[x][y] == "1" :
            grid[x][y] = "0"
            self.bfs(grid,x+1,y)
            self.bfs(grid,x,y+1)
            self.bfs(grid,x-1,y)
            self.bfs(grid,x,y-1)
            return True
        return False