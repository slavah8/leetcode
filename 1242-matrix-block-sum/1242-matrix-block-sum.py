class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        matrix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += mat[r][c]
                above = matrix_sum[r][c + 1]
                matrix_sum[r + 1][c + 1] = prefix + above
        print(matrix_sum)

        ans = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            r1 = max(0, r - k)
            r2 = min(rows - 1, r + k)
            for c in range(cols):
                c1 = max(0, c - k)
                c2 = min(cols - 1, c + k)
                bottom_right = matrix_sum[r2 + 1][c2 + 1]
                left = matrix_sum[r2 + 1][c1]
                top_left = matrix_sum[r1][c1]
                above = matrix_sum[r1][c2 + 1]
                ans[r][c] = bottom_right - left - above + top_left
        return ans