class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        def idx(c):
            return ord(c) - ord('a')
        
        for i, ch in enumerate(s):
            j = idx(ch)
            if first[j] == -1:
                first[j] = i
            last[j] = i

        
        ans = 0
        # for every possible letter
        # fix x -> xyx count how many unique letters in between x there are and add to answer
        for x in range(26):
            L = first[x]
            R = last[x]
            if L != -1 and L < R:
                seen_mid = set(s[L + 1: R])
                ans += len(seen_mid)
        return ans
