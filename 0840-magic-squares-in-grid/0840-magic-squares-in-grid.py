class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        squares = 0

        
        def is_magic(r0, c0):
            seen = [False] * 10
            
            for r in range(r0, r0 + 3):
                for c in range(c0, c0 + 3):
                    x = grid[r][c]
                    if x > 9 or x < 1:
                        return False
                    if seen[x]:
                        return False
                    seen[x]= True

            # row sums
            target = grid[r0][c0] + grid[r0][c0 + 1] + grid[r0][c0 + 2]
            row_sum = 0
            
            for c in range(c0, c0 + 3):
                row_sum += grid[r0][c]
            
            for r in range(r0 + 1, r0 + 3):
                cur_sum = 0
                for c in range(c0, c0 + 3):
                    cur_sum += grid[r][c]
                if cur_sum != row_sum:
                    return False
            
            # col sums
            col_sum = 0
            for r in range(r0, r0 + 3):
                col_sum += grid[r][c0]
            
            for c in range(c0 + 1, c0 + 3):
                cur_sum = 0
                for r in range(r0, r0 + 3):
                    cur_sum += grid[r][c]
                if cur_sum != col_sum:
                    return False

            diag1 = grid[r0][c0] + grid[r0 + 1][c0 + 1] + grid[r0 + 2][c0 + 2]
            if diag1 != target:
                return False
            
            diag2 = grid[r0][c0 + 2] + grid[r0 + 1][c0 + 1] + grid[r0 + 2][c0]
            if diag2 != target:
                return False
            
            return True
            

        for r in range(0, rows - 3 + 1):
            for c in range(0, cols - 3 + 1):
                if is_magic(r, c):
                    squares += 1
        return squares
