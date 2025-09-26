class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
        MOD = modulo
        freq = defaultdict(int) # how many counts at L index
        freq[0] = 1

        ans = 0
        prefix = 0
        for x in nums:
            if x % MOD == k:
                prefix += 1
            # prefix[R] - need == k
            # -need = k - prefix[R]
            # need = prefix[R] - k
            rem = prefix % MOD
            need = (rem - k) % MOD
            ans += freq[need]
            freq[rem] += 1
        return ans