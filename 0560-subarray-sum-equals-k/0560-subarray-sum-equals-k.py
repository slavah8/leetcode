class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        freq = collections.Counter({0 : 1})
        prefix = 0
        ans = 0
        for x in nums:
            prefix += x
            ans += freq[prefix - k]
            freq[prefix] += 1
        return ans