class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        
        print(prefix)
        INF = 10 ** 10
        ans = INF
        for j in range(1, n + 1):
            i_lo = max(0, j - r)
            i_hi = j - l
            
            if i_lo > i_hi:
                continue

            for i in range(i_lo, i_hi + 1):
                summ = prefix[j] - prefix[i]
                if summ > 0 and summ < ans:
                    ans = summ

        return ans if ans != INF else -1
