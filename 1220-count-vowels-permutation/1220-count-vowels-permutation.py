class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        from functools import lru_cache
import sys

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        sys.setrecursionlimit(1000000)

        @lru_cache(None)
        def dp(prev_letter: str, length: int) -> int:
            if length == n:
                return 1

            ways = 0

            if prev_letter == 'a':
                ways = (ways + dp('e', length + 1)) % MOD

            elif prev_letter == 'e':
                ways = (ways + dp('a', length + 1)) % MOD
                ways = (ways + dp('i', length + 1)) % MOD

            elif prev_letter == 'i':
                ways = (ways + dp('a', length + 1)) % MOD
                ways = (ways + dp('e', length + 1)) % MOD
                ways = (ways + dp('o', length + 1)) % MOD
                ways = (ways + dp('u', length + 1)) % MOD

            elif prev_letter == 'o':
                ways = (ways + dp('i', length + 1)) % MOD
                ways = (ways + dp('u', length + 1)) % MOD

            else:  # prev_letter == 'u'
                ways = (ways + dp('a', length + 1)) % MOD

            return ways

        total = 0
        for ch in ('a', 'e', 'i', 'o', 'u'):
            total = (total + dp(ch, 1)) % MOD

        return total
