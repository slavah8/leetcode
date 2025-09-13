class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sum_matrix[r][c + 1]
                self.sum_matrix[r + 1][c + 1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1 = row1 + 1
        col1 = col1 + 1
        row2 = row2 + 1
        col2 = col2 + 1
        bottom_right = self.sum_matrix[row2][col2]
        above = self.sum_matrix[row1 - 1][col2]
        left = self.sum_matrix[row2][col1 - 1]
        top_left = self.sum_matrix[row1 - 1][col1 - 1]
        
        
        return bottom_right - left - above + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)