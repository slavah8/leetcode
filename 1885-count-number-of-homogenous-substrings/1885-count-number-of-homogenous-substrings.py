class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        ans = 0
        run_len = 0
        prev = None
        for char in s:
            if char == prev:
                run_len += 1
            else:
                run_len = 1
                prev = char
            ans = ans + (run_len) % MOD
        return ans % MOD