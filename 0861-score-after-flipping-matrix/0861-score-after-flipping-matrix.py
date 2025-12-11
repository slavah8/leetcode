class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            if grid[r][0] == 0:
                # flip
                for c in range(cols):
                    grid[r][c] = 1 - grid[r][c]
        
        

        # count_ones + count_zeroes == rows
        # rows - count_ones == count_zeroes
        # 
        for c in range(cols):
            count_ones = 0
            for r in range(rows):
                if grid[r][c] == 1:
                    count_ones += 1
            if count_ones < (rows - count_ones):
                # flip
                for r in range(rows):
                    grid[r][c] = 1 - grid[r][c]
        
        total = 0
        for r in range(rows):
            row_sum = 0
            for c in range(cols):
                if grid[r][c] == 1:
                    row_sum += (1 << (cols - c - 1))
            print(row_sum)
            total += row_sum
        return total
