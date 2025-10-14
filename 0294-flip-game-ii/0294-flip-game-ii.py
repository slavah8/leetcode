class Solution:
    def canWin(self, currentState: str) -> bool:
        
        
        # Define win(s) = True if the player to move from state s has a forced win
        #  (i.e., can move so that the opponent         eventually has no legal moves), else False.
        @lru_cache(None)
        def win(s):
            N = len(s)
            for i in range(N - 1):
                if s[i] == "+" and s[i + 1] == "+":
                    new_state = s[:i] + "--" + s[i + 2:]
                    if not win(new_state):
                        return True
            return False
            
        return win(currentState)