class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            board[r][c] = '#'

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'X':
                    dfs(nr, nc)



            
        total = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    total += 1
                    dfs(r, c)
        return total