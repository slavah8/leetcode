class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        counts = collections.Counter(s)
        
        odd_chars = [ch for ch, c in counts.items() if c % 2 == 1]

        if len(odd_chars) > 1:
            return []
        
        mid = odd_chars[0] if odd_chars else ''

        need = {ch : c // 2 for ch, c in counts.items()}
        half_len = sum(need.values())

        res, path = [], []
        def backtrack():
            if len(path) == half_len:
                half = ''.join(path)
                res.append(half + mid + half[::-1])
                return
            
            for ch in need:
                if need[ch] > 0:
                    # choose
                    need[ch] -= 1
                    path.append(ch)
                    backtrack()
                    need[ch] += 1
                    path.pop()
        
        backtrack()     
        return res
                
                
        
