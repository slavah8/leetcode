class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        best = 0
        if len(tokens) == 0:
            return 0
        tokens.sort()
        if power < min(tokens):
            return 0
        print(tokens)
        l = 0
        r = len(tokens) - 1
        score = 0
        while l <= r:
            # greedily always increase score if possible
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            else:
                # always get as much power as possible
                if score >= 1:
                    power += tokens[r]
                    score -= 1
                    r -= 1
            print(score)
            best = max(best, score)
        return best
            
