class Solution:
    def numSplits(self, s: str) -> int:
        
        n = len(s)

        right_freq = [0] * 26

        for ch in s:
            right_freq[ord(ch) - 97] += 1
        
        right_distinct = sum(1 for f in right_freq if f > 0)

        left_seen = [0] * 26
        left_distinct = 0
        good = 0

        for i in range(n):

            ch = s[i]
            if left_seen[ord(ch) - 97] == 0:
                left_distinct += 1

            left_seen[ord(ch) - 97] += 1
            right_freq[ord(ch) - 97] -= 1
            if right_freq[ord(ch) - 97] == 0:
                right_distinct -= 1

            if left_distinct == right_distinct:
                good += 1
        
        return good
