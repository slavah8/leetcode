class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        def is_valid(r0, c0):
            counts = defaultdict(int)

            for r in range(r0, r0 + 2):
                for c in range(c0, c0 + 2):
                    x = grid[r][c]
                    counts[x] += 1
            print(counts)
            for color, frq in counts.items():
                if frq >= 3:
                    return True
            return False

        for start_r in range(0, rows - 2 + 1):
            for start_c in range(0, cols - 2 + 1):
                if is_valid(start_r, start_c):
                    return True
        
        return False
