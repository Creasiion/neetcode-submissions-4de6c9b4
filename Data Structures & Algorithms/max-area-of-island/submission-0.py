class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0 
        directions = [(1,0), (0,1),(-1,0), (0,-1)]
        m = len(grid)
        n = len(grid[0])
        areas = []
        self.currArea = 1
        seen = set()

        def isValid(row, col):
            return row < m and row >= 0 and col < n and col >= 0 and grid[row][col] == 1

        def dfs(row, col):
            for x,y in directions:
                nextRow = row + x
                nextCol = col + y
                if isValid(nextRow, nextCol) and (nextRow, nextCol) not in seen:
                    self.currArea += 1
                    seen.add((nextRow,nextCol))
                    dfs(nextRow, nextCol)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row,col) not in seen: # Found some kind of island!
                    seen.add((row,col))
                    dfs(row, col)
                    areas.append(self.currArea)
                    self.currArea = 1
        return max(areas) if areas else 0