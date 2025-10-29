class Solution:
    def makeArrayPositive(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        
        bad = []
        for L in (3, 4, 5):
            for i in range(n - L + 1):
                if prefix[i + L] - prefix[i] <= 0:
                    bad.append((i, i + L)) # (L, R)
        if not bad:
            return 0
        
        bad.sort(key = lambda x: x[1])
        INF = 10 ** 10
        last = INF
        ops = 0
        for L, R in bad:
            if not (L <= last < R):
                ops += 1
                last = R - 1
        return ops