class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])

        self.mat = [row[:] for row in matrix]
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        
        for r in range(self.m):
            for c in range(self.n):
                self.add(r + 1, c + 1, matrix[r][c])
    
    def add(self, r, c, delta):
        i = r
        while i <= self.m:
            j = c
            while j <= self.n:
                self.bit[i][j] += delta
                j += j & -j
            i += i & -i
    
    def prefix_sum(self, r, c):
        res = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                res += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return res

    def update(self, row: int, col: int, val: int) -> None:
        old = self.mat[row][col]
        delta = val - old
        self.mat[row][col] = val
        self.add(row + 1, col + 1, delta)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1

        bot_right = self.prefix_sum(r2, c2)
        left = self.prefix_sum(r2, c1 - 1)
        top  = self.prefix_sum(r1 - 1, c2)
        top_left = self.prefix_sum(r1 - 1, c1 - 1)
        return bot_right - left - top + top_left

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)