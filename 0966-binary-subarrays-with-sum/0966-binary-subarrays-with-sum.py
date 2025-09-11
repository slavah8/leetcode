class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        freq = collections.Counter({0 : 1})
        ans = 0

        for x in nums:
            prefix += x
            ans += freq[prefix - goal]
            freq[prefix] += 1
        
        return ans