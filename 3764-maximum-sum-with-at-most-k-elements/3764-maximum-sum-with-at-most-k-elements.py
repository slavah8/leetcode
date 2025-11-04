class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        summ = 0

        rows = len(grid)
        cols = len(grid[0])

        heap = [] # (val, row, col)
        for r in range(rows):
            for c in range(cols):
                heapq.heappush(heap, (-grid[r][c], r, c))
        
        
        while k > 0 and heap:
            val, r, c = heapq.heappop(heap)
            
            if limits[r] == 0:
                continue
            val = -val
            limits[r] -= 1
            summ += val
            k -= 1
        return summ

