class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        masks = []

        for w in arr:
            m = 0
            ok = True
            for char in w:
                bit = 1 << (ord(char) - ord('a'))
                if m & bit:
                    ok = False
                    break
                m |= bit
            if ok:
                masks.append((m, len(w)))
        
        best = 0
        def dfs(i, mask, length):
            nonlocal best
            if length > best:
                best = length
            
            for j in range(i, len(masks)):
                wmask, wlen = masks[j]
                if (mask & wmask) == 0:
                    dfs(j + 1, mask | wmask, length + wlen)
        dfs(0, 0, 0)
        return best
                
