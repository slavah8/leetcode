class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        pair_count = defaultdict(int)
        total = 0

        for r in range(rows):
            ones = []
            for c in range(cols):
                if grid[r][c] == 1:
                    ones.append(c)
            
            for i in range(len(ones)):
                for j in range(i + 1, len(ones)):
                    total += pair_count[(ones[i], ones[j])]
                    pair_count[(ones[i], ones[j])] += 1
        
        return total
            