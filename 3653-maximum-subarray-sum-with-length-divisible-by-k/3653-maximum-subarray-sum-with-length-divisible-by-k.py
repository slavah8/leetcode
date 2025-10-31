class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10 ** 15
        # min_pref[r] is the smallest prefix sum seen so far among indices i with i % k == r
        min_pref = [INF] * k
        min_pref[0] = 0
        best = -INF
        prefix = 0
        for j, x in enumerate(nums, 1):
            prefix += x
            r = j % k

            best = max(best, prefix - min_pref[r])
            
            if prefix < min_pref[r]:
                min_pref[r] = prefix
        
        return best

