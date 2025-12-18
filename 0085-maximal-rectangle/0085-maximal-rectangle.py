class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        left = [0] * cols # Leftmost column index (inclusive) where a rectangle of height height[c] can start
        right = [cols] * cols # Rightmost column index (exclusive) where that rectangle can end
        best = 0
        for r in range(rows):
            cur_left = 0 # The earliest column a rectangle can start in this row, because anything left of this crosses a 0
            cur_right = cols # The latest column (exclusive) a rectangle can end at in this row, because anything at/after this crosses a 0.”
            for c in range(cols):

                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # update left boundaries
            for c in range(cols):
                if matrix[r][c] == '1':
                    left[c] = max(left[c], cur_left)
                else:
                    left[c] = 0
                    cur_left = c + 1

            # update right boundaires
            for c in range(cols - 1, -1, -1):
                if matrix[r][c] == '1':
                    right[c] = min(cur_right, right[c])
                else:
                    right[c] = cols
                    cur_right = c
            
            for c in range(cols):
                best = max(best, heights[c] * (right[c] - left[c]))
            print(heights, left, right)
            
            
        return best


