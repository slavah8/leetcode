class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for _ in range(cols):
            global_max = 0
            row_remove = 0
            for r, row in enumerate(grid):
                local_max = 0
                for c, x in enumerate(row):
                    if x > global_max:
                        global_max = x

                    if x > local_max:
                        local_max = x
                    
                row.remove(local_max)
            
            ans += global_max
            print(grid)
                

        return ans

                
