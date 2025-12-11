class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        

        rows = len(matrix)
        cols = len(matrix[0])

        for start_col in range(cols):
            val = matrix[0][start_col]
            r, c = 1, start_col + 1
            while r < rows and c < cols:
                if val != matrix[r][c]:
                    return False
                r += 1
                c += 1
        
        for start_row in range(1, rows):
            val = matrix[start_row][0]
            r, c = start_row + 1, 1
            while r < rows and c < cols:
                if val != matrix[r][c]:
                    return False
                r += 1
                c += 1
        return True