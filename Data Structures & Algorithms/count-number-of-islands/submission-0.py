class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        numIslands = 0
        directions = [(0,1), (1,0),(-1,0), (0,-1)]

        def isValid(currRow, currCol):
            return currRow < rows and currRow >= 0 and currCol < cols and currCol >= 0 and grid[currRow][currCol] == '1'

        def dfs(row, col):
            for x, y in directions:
                nextRow = row + x
                nextCol = col + y
                if isValid(nextRow,nextCol) and (nextRow, nextCol) not in seen:
                    seen.add((nextRow, nextCol))
                    dfs(nextRow, nextCol)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    seen.add((r,c))
                    dfs(r, c)
                    numIslands += 1
        return numIslands