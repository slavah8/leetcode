class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + nums[i]
        total = prefix[N]
        print(prefix)
        ans = 0
        for i in range(1, N - 1):
            # left = nums[0..i-1] → sum L = pre[i]
            # mid = nums[i..j-1] → sum M = pre[j] - pre[i]
            # right = nums[j..n-1] → sum R = pre[n] - pre[j]

            # L ≤ M ⇒ pre[i] ≤ pre[j] - pre[i] ⇒ pre[j] ≥ 2·pre[i]
            # M ≤ R ⇒ pre[j] - pre[i] ≤ pre[n] - pre[j] ⇒ pre[j] ≤ (pre[n] + pre[i]) / 2

            #   pre[j] >= 2*L        (left <= mid)
            #   pre[j] <= (total+L)/2 (mid <= right)
            L = prefix[i]
        
            j_low = bisect.bisect_left(prefix, 2 * L, lo = i + 1, hi = N)
            target = (total + L) // 2
            j_high = bisect.bisect_right(prefix, target, lo = i + 1, hi = N) - 1

            j_low = max(i + 1, j_low)
            j_high = min(N - 1, j_high)
            if j_low <= j_high:
                ans = (ans + (j_high - j_low + 1)) % MOD
        return ans % MOD