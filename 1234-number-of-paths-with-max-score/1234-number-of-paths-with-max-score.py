class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        rows = len(board)
        cols = len(board[0])
        INF = 10 ** 15
        # max sum collectible to reach cell (i, j) from E
        score = [[-INF] * cols for _ in range(rows)]
        # ways[i][j] = # of paths that achieve score[i][j]
        ways = [[0] * cols for _ in range(rows)]

        def val(i, j):
            char = board[i][j]
            if char in 'ES':
                return 0
            if char == 'X':
                return None # blocked
            return ord(char) - ord('0')
    
        if board[0][0] == 'X':
            return [0, 0]

        score[0][0] = 0
        ways[0][0] = 1

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                if board[i][j] == 'X':
                    continue
                
                best_prev = -INF
                count = 0

                # up left or diag
                for pi, pj in ((i - 1, j), (i, j - 1), (i - 1, j - 1)):
                    if 0 <= pi < rows and 0 <= pj < cols and ways[pi][pj] > 0:
                        if score[pi][pj] > best_prev:
                            best_prev = score[pi][pj]
                            count = ways[pi][pj]
                        elif score[pi][pj] == best_prev:
                            count = (count + ways[pi][pj]) % MOD

                cell_val = val(i, j)
                score[i][j] = best_prev + (cell_val or 0)
                ways[i][j] = count % MOD
                
        if ways[rows - 1][cols - 1] == 0:
            return [0, 0]
        return [score[rows - 1][cols - 1], ways[rows - 1][cols - 1]]
                        




