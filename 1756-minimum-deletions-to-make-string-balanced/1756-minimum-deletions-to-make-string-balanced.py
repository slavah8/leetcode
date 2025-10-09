class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        dp = 0 # min deletions to make prefix balanced
        # need all a's to come before the b's
        # choices:
        # either delete the current 'a' or delete all b's before this a
        b_count = 0
        for i, char in enumerate(s):
            if char == 'b':
                b_count += 1
            else:
                dp = min(dp + 1, b_count)
        return dp
