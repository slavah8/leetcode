class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        # how many elements in matrix are <= x
        def count_le(x):
            count = 0
            r = 0
            c = cols - 1
            while r < rows and c >= 0:
                if matrix[r][c] > x: # we can eliminate the column
                    c -= 1
                else:
                    count += c + 1 # everything in this row is <= x so we count it then move down
                    r += 1
            return count
        
        low = matrix[0][0]
        high = matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2

            if count_le(mid) >= k: # more elements smaller than k
                high = mid
            else:
                low = mid + 1
        return high
        




        

        