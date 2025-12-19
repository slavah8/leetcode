class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        rows = len(board)
        cols = len(board[0])

        while True:
            crush = [[False] * cols for _ in range(rows)]
            changed = False
            for r in range(rows):
                # mark horizontal
                c = 0
                while c < cols:
                    v = board[r][c]
                    if v == 0:
                        c += 1
                        continue
                    
                    j = c
                    while j < cols and board[r][j] == v:
                        j += 1
                    if j - c >= 3:
                        changed = True
                        for k in range(c, j):
                            crush[r][k] = True
                    c = j
                
            # mark vertical
            for c in range(cols):
                r = 0
                while r < rows:
                    v = board[r][c]
                    if v == 0:
                        r += 1
                        continue
                    
                    i = r
                    while i < rows and board[i][c] == v:
                        i += 1
                    
                    if i - r >= 3:
                        changed = True
                        for k in range(r, i):
                            crush[k][c] = True
                    r = i

            if not changed:
                return board

            for r in range(rows):
                for c in range(cols):
                    if crush[r][c]:
                        board[r][c] = 0
            
            for c in range(cols):
                write = rows - 1
                for r in range(rows - 1, -1, -1):
                    if board[r][c] != 0:
                        board[write][c] = board[r][c]
                        write -= 1
            
                for r in range(write, -1, -1):
                    board[r][c] = 0
                            
                    
            


