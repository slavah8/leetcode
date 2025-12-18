class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        ops = 0
        for c in range(cols):
            initial = grid[0][c]
            for r in range(1, rows):
                x = grid[r][c]
                print(initial, x)
                if x > initial:
                    initial = x
                    continue
                else:
                    diff = abs(initial - x)
                    ops += (diff + 1)
                    initial = x + (diff + 1)
            print(ops)

        return ops
