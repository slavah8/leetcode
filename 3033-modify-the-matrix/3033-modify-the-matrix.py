class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        max_cols = [-1] * cols
        for c in range(cols):
            maxx = -1
            for r in range(rows):
                x = matrix[r][c]
                if x > maxx:
                    maxx = x
            max_cols[c] = maxx
        
        print(max_cols)
        for r in range(rows):
            for c in range(cols):
                x = matrix[r][c]
                if x == -1:
                    matrix[r][c] = max_cols[c]
        
        return matrix

