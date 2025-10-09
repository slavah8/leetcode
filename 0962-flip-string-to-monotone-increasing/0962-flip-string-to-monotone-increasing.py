class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        

        dp = 0 
        count_ones = 0
        for index, char in enumerate(s):
            if char == '1':
                count_ones += 1
            else:
                dp = min(dp + 1, count_ones)
        return dp