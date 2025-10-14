class Solution:
    def longestAwesome(self, s: str) -> int:
        # A substring can form a palindrome ↔ at most one bit set in its parity mask.
        # substring_mask == 0       # all even counts
        # or substring_mask == (1 << b)  for some b


        
        N = len(s)
        INF = N + 1
        # 1024 = 2^10 possible bitmasks
        first = [INF] * (1 << 10)
        first[0] = -1 # first[mask] = earliest index where this prefix parity mask appeared

        mask = 0
        best = 0
        for i, char in enumerate(s):
            d = ord(char) - ord('0')

            mask ^= (1 << d)

            # case A: all even counts in the substring
            if first[mask] != INF:
                best = max(best, i - first[mask])
            
            # case B: exactly one odd count (flip one bit)
            for b in range(10):
                cand = mask ^ (1 << b)
                if first[cand] != INF:
                    best = max(best, i - first[cand])
            
            if first[mask] == INF:
                first[mask] = i
        return best
        

