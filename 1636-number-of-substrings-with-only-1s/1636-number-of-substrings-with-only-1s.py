class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        prev = None
        run_len = 0
        ans = 0
        for char in s:
            if char == '1':
                run_len += 1
                prev = '1'
            else:
                run_len = 0
                prev = '0'
            ans = ans + run_len % MOD
        return ans % MOD