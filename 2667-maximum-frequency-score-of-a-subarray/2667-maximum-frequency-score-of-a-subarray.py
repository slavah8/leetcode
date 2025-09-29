class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = 10 ** 9 + 7
        score = 0
        freq = defaultdict(int)

        def add_delta(x, old, new):
            nonlocal score
            if old > 0:
                score = (score - pow(x, old, MOD)) % MOD
            if new > 0:
                score = (score + pow(x, new, MOD)) % MOD

        for i in range(k):
            x = nums[i]
            old = freq[x]
            freq[x] += 1
            add_delta(x, old, old + 1)
        
        best = score
        for r in range(k, N):
            x_out = nums[r - k]
            x_in = nums[r]

            old = freq[x_out]
            freq[x_out] -= 1
            add_delta(x_out, old, old - 1)
            if freq[x_out] == 0:
                del freq[x_out]

            old = freq[x_in]
            freq[x_in] += 1
            add_delta(x_in, old, old + 1)

            if score > best:
                best = score

        return best % MOD
