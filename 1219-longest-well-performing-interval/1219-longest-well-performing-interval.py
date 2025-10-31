class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        tiring = []
        for h in hours:
            if h > 8:
                tiring.append(1)
            else:
                tiring.append(-1)
        
        prefix = 0
        best = 0
        seen = {0 : -1} # prefix : idx
        
        for i, h in enumerate(tiring):
            prefix += h

            if prefix >= 1:
                best = max(best, i + 1)
            else:
                # -2 - (-3) = 1
                if prefix - 1 in seen:
                    best = max(best, i - seen[prefix - 1])
                
            if prefix not in seen:
                seen[prefix] = i
        return best


            

            

                

