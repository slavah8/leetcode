class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        m = n // 3 # number of threes
        r = n % 3 # reminader

        if r == 0:
            return 3 ** m
        elif r == 1:
            return (3 ** (m - 1)) * 4
        else:
            return (3 ** m) * 2
