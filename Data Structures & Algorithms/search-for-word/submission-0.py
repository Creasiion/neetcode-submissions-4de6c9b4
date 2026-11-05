class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        IDEA: Using backtracking
        - Since the same cell can't be used multiple times, we'd do direction + 1 for our backtracking
        What we could do is append the letters to result, so if 
        'word' is in arr we can just return True, and we can add return false outside of the for loop, since that means we backtracked through all the answers.
        Directions we can go is up down left right
        (0,1) (0,-1) (-1,0) (1,0) 
        We can instantly prune when the letter doesn't exist in word
        i.e. if char (B) not in CAT, get off this branch
        '''
        visited = set()
        directions = [(0,1), (0,-1), (-1,0), (1,0) ]
        def isValid(row, col):
           return 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in visited
        def backtracking(row, col, currCharTarget):
            if board[row][col] == word[currCharTarget]:
                visited.add((row, col))
                if currCharTarget == len(word) -1:
                    return True
                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc
                    if isValid(newRow, newCol):
                        if backtracking(newRow, newCol, currCharTarget + 1): 
                            return True
                visited.remove((row, col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtracking(row, col, 0):
                    return True
        return False

