class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # start at top right corner 
        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        c = cols - 1

        while r < rows and c >= 0:
            if matrix[r][c] > target: # we can eliminate the entire column
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        
        return False
