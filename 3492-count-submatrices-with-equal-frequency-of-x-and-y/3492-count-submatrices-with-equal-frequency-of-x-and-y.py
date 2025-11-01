class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sum_matrix = [[0] * cols for _ in range(rows)]
        count_x = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            run = 0
            run_x = 0
            for c in range(cols):
                if grid[r][c] == 'X':
                    run += 1
                    run_x += 1
                elif grid[r][c] == 'Y':
                    run -= 1
                sum_matrix[r][c] = run + (sum_matrix[r - 1][c] if r > 0 else 0)
                count_x[r][c] = run_x + (count_x[r - 1][c] if r > 0 else 0)
        
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if sum_matrix[r][c] == 0 and count_x[r][c] > 0:
                    ans += 1
        return ans