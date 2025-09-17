class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])

        matrix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += mat[r][c]
                above = matrix_sum[r][c + 1]
                matrix_sum[r + 1][c + 1] = prefix + above
        
        def rec_sum(r1, c1, r2, c2):
            R1, C1 = r1 + 1, c1 + 1
            R2, C2 = r2 + 1, c2 + 1

            bottom_right = matrix_sum[R2][C2]
            left = matrix_sum[R2][C1 - 1]
            above = matrix_sum[R1 - 1][C2]
            top_left = matrix_sum[R1 - 1][C1 - 1]
            return bottom_right - left - above + top_left

        def can(k):
            if k == 0:
                return True
            for r in range(rows - k + 1):
                rr = r + k - 1
                for c in range(cols - k + 1):
                    cc = c + k - 1
                    if rec_sum(r, c, rr, cc) <= threshold:
                        return True
            return False
        
        low, high = 0, min(rows, cols)
        best = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid): # try bigger k
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best

