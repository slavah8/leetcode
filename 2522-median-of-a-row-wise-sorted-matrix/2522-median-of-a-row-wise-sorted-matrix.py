class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])

        K = (R * C) // 2 + 1
        low = min(row[0] for row in grid)
        high = max(row[-1] for row in grid)

        while low < high:
            mid = (low + high) // 2
            cnt = 0
            for row in grid:
                cnt += bisect.bisect_right(row, mid)
            
            if cnt >= K:
                high = mid
            else:
                low = mid + 1
        
        return low


