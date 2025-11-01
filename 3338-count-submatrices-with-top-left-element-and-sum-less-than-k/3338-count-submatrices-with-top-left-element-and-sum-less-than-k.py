class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] > k:
            return 0
        
        sum_matrix = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            run = 0
            for c in range(cols):
                run += grid[r][c]
                sum_matrix[r][c] = run + (sum_matrix[r - 1][c] if r > 0 else 0)
        print(sum_matrix)

        ans = 0
        c = cols - 1 # rightmost candidate
        for r in range(rows):
            while c >= 0 and sum_matrix[r][c] > k:
                c -= 1
            ans += (c + 1)
            if c < 0:
                break
        return ans

