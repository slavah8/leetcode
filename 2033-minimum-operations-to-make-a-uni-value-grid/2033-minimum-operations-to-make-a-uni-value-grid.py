class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        full = []
        for r in range(rows):
            for c in range(cols):
                full.append(grid[r][c])
        
        full.sort()
        if len(full) == 1:
            return 0
        
        base = full[0] % x
        for num in full:
            if num % x != base:
                return -1

        med = full[len(full) // 2]
        print(full)
        print(med)
        ops = 0
        # num = 
        for num in full:
            ops += abs(num - med) // x
        return ops


            
                