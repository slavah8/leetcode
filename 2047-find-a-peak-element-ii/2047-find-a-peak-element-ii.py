class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        left = 0
        right = cols - 1
        # eliminate columns, go thru each column and find the row with the greatest value then check the left and right
        # and eliminate accordingly
        while left <= right:
            
            mid = (left + right) // 2
            # find row with max
            row = max(range(rows), key = lambda i: mat[i][mid])
            curr = mat[row][mid]
            # compare with left and right values
            left_val = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[row][mid + 1] if mid + 1 < cols else -1
            if right_val > curr: # search the right
                left = mid + 1
            elif left_val > curr:
                right = mid - 1
            else:
                return [row, mid]



