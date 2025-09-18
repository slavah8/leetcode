class Solution:
    def maxPower(self, s: str) -> int:
        prev = None
        run_len = 0
        ans = 0
        for char in s:
            if char == prev:
                run_len += 1
            else:
                run_len = 1
                prev = char
            ans = max(ans, run_len)
        return ans