class Solution:
    def findKthNumber(self, r: int, c: int, k: int) -> int:
        
        # how many elements in matrix <= x
        def count_le(x):
            # start at top right corner
            row = 1
            col = c
            cnt = 0
            while row <= r and col >= 1:
                if row * col > x: # we can eliminate the column
                    col -= 1
                else:
                    cnt += col
                    row += 1
            return cnt

        low = 1
        high = (r) * (c)
        
        while low < high:
            mid = (low + high) // 2

            if count_le(mid) >= k: # shrink
                high = mid
            else:
                low = mid + 1
        
        return low