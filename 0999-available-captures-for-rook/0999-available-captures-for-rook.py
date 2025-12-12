class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        rows = len(board)
        cols = len(board[0])

        start_r = 0
        start_c = 0
        count = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'R':
                    start_r = r
                    start_c = c
                    break
        

        # try up
        for r in range(start_r, -1, -1):
            if board[r][start_c] == '.':
                continue
            
            if board[r][start_c] == 'p':
                count += 1
                break
            
            if board[r][start_c] == 'B':
                break

        for r in range(start_r, rows):
            if board[r][start_c] == '.':
                continue
            
            if board[r][start_c] == 'p':
                count += 1
                break
            
            if board[r][start_c] == 'B':
                break
        
        # try left
        for c in range(start_c,-1,-1):
            if board[start_r][c] == '.':
                continue
            
            if board[start_r][c] == 'p':
                count += 1
                break
            
            if board[start_r][c] == 'B':
                break
        
        for c in range(start_c, cols):
            if board[start_r][c] == '.':
                continue
            
            if board[start_r][c] == 'p':
                count += 1
                break
            
            if board[start_r][c] == 'B':
                break
        
        return count

