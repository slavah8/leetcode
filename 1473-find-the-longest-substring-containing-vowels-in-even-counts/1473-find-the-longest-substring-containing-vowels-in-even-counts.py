class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u':4}

        state = 0 # 00000 bitmask
        first = {0: -1}          # mask -> earliest index
        best = 0
        
        for j, char in enumerate(s):
            if char in idx:
                state ^= (1 << idx[char])

            if state in first: # we've seen this bitmask so valid
                best = max(best, j - first[state])
            else:
                first[state] = j
        return best