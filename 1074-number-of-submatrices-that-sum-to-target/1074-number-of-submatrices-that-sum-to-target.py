class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        for top in range(rows):
            col_sum = [0] * cols

            for bottom in range(top, rows):
                for c in range(cols):
                    col_sum[c] += matrix[bottom][c]

                prefix = 0
                freq = defaultdict(int)
                freq[0] = 1 
                for x in col_sum:
                    prefix += x
                    ans += freq[prefix - target]
                    freq[prefix] += 1
        return ans

