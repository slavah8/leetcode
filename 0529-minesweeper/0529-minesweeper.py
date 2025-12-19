class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]


        def dfs(r, c):
            x = board[r][c]

            if x == 'E':
                count = 0
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 'M':
                            count += 1
                if count > 0:
                    board[r][c] = str(count)
                    return
                else:
                    board[r][c] = 'B'
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'E':
                            dfs(nr, nc)
            
        

        start_r, start_c = click
        if board[start_r][start_c] == 'M':
            board[start_r][start_c] = 'X'
            return board
        dfs(start_r, start_c)
        return board
