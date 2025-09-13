class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        row_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += grid[r][c]
                row_prefix[r][c + 1] = prefix
        print(row_prefix)

        def row_segment_sum(r, c1, c2):
            return row_prefix[r][c2 + 1] - row_prefix[r][c1]

        best = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                top = row_segment_sum(r, c, c + 2)
                middle = grid[r + 1][c + 1]
                bottom = row_segment_sum(r + 2, c, c + 2)
                hourglass_sum = top + middle + bottom
                if hourglass_sum > best:
                    best = hourglass_sum
        return best