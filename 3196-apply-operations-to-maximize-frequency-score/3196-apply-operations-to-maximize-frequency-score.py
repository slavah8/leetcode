class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        N = len(nums)

        prefix = [0] * (N + 1)

        for i in range(N):
            prefix[i + 1] = prefix[i] + a[i]

        def range_sum(L, R):
            return prefix[R + 1] - prefix[L]

        L = 0
        ans = 1
        for R in range(N):
            while True:
                m = (L + R) // 2
                left_size = m - L
                left_sum = range_sum(L, m - 1) if left_size > 0 else 0
                left_cost = a[m] * left_size - left_sum

                right_size = R - m
                right_sum = range_sum(m + 1, R) if right_size > 0 else 0
                right_cost = right_sum - a[m] * right_size
                total_cost = left_cost + right_cost
                
                if total_cost <= k:
                    break
                L += 1
            ans = max(ans, R - L + 1)
        return ans
                
                 