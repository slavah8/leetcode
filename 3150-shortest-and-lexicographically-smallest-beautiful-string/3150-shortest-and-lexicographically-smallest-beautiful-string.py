class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        N = len(s)
        left = 0
        ones = 0
        best = None

        for right, char in enumerate(s):
            if char == "1":
                ones += 1
            
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1
            
            if ones == k:
                while s[left] == '0':
                    left += 1
                cand = s[left:right + 1]
                if best is None or len(cand) < len(best) or (len(cand) == len(best) and cand < best):
                    best = cand
                if s[left] == '1':
                    ones -= 1
                left += 1
            
        return best if best else ""


             

