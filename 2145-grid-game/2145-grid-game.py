class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # robot 1s choice when to go down a row
        # he has n choices from col 0 ... n
        
        top_suffix = [0] * cols
        

        top_suffix[cols - 1] = grid[0][cols - 1]
        for c in range(cols - 2, -1, -1):
            top_suffix[c] = top_suffix[c + 1] + grid[0][c]
        print(top_suffix)

        bot_prefix = [0] * cols
        bot_prefix[0] = grid[1][0]
        for c in range(1, cols):
            bot_prefix[c] = bot_prefix[c - 1] + grid[1][c]
        print(bot_prefix)
        INF = 10 ** 10
        best = INF
        for i in range(cols):
        # Imagine the first robot goes across the top row until column i, then drops down, then finishes along the bottom row.
            # second robots score is (i + 1, ..., n) and bottom 0 ... i - 1
            # if robot 1 drops down at this ith column robot 2 gets top_suffix[cols - 1] - top_suffix[i + 1] and 
            # bot_prefix[i] - bot_prefix[0] 

            top_right = top_suffix[i + 1] if i + 1 < cols else 0
            bot_left =  bot_prefix[i - 1] if i - 1 >= 0 else 0
            cand = max(top_right, bot_left)
            best = min(best, cand)
        
        return best



            

