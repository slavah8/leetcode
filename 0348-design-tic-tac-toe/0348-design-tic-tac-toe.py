class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, r: int, c: int, player: int) -> int:
        add = 1 if player == 1 else -1
        self.rows[r] += add
        self.cols[c] += add

        if r == c:
            self.diag += add
        if r + c == self.n - 1:
            self.anti += add
        
        if (abs(self.rows[r]) == self.n or abs(self.cols[c]) == self.n or abs(self.diag) == self.n or abs(self.anti) == self.n):
            return player
        return 0
        


        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)