class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        n = len(s)
        l = 0
        char_freq = defaultdict(int)
        best = 0
        for r in range(n):
            ch = s[r]

            char_freq[ch] += 1
            while char_freq[ch] > 2:
                ch_left = s[l]
                char_freq[ch_left] -= 1
                l += 1
            

            
            best = max(best, r - l + 1)
        return best


