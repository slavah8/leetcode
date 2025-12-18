class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        

    def adjacentSum(self, value: int) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(self.rows):
            for c in range(self.cols):
                x = self.grid[r][c]
                if x == value:
                    start_r, start_c = r, c
        
        count = 0
        total = 0
        for dr, dc in directions:
            nr, nc = start_r + dr, start_c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                x = self.grid[nr][nc]
                total += x
                count += 1
        
        return total    

    def diagonalSum(self, value: int) -> int:
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for r in range(self.rows):
            for c in range(self.cols):
                x = self.grid[r][c]
                if x == value:
                    start_r, start_c = r, c
        
        total = 0
        count = 0
        for dr, dc in directions:
            nr, nc = start_r + dr, start_c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                x = self.grid[nr][nc]
                total += x
                count += 1
        
        return total

        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)