class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += grid[r][c]
                above = sum_matrix[r][c + 1]
                sum_matrix[r + 1][c + 1] = prefix + above
        
        
        def rect_sum(r1, c1, r2, c2):
            bottom_right = sum_matrix[r2 + 1][c2 + 1]
            left = sum_matrix[r2 + 1][c1]
            top = sum_matrix[r1][c2 + 1]
            top_left = sum_matrix[r1][c1]
            return bottom_right - left - top + top_left


        max_side = min(rows, cols)

        for k in range(max_side, 0, -1):
            for r in range(rows - k + 1):
                for c in range(cols - k + 1):
                    r2, c2 = r + k - 1, c + k - 1

                    top = rect_sum(r, c, r, c2)
                    bot = rect_sum(r2, c, r2, c2)
                    left = rect_sum(r, c, r2, c)
                    right = rect_sum(r, c2, r2, c2)

                    if top == k and bot == k and left == k and right == k:
                        return k * k

        return 0
                    
                    
