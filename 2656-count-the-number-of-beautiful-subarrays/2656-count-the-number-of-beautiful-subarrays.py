class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        

        freq = collections.defaultdict(int) # freq[prefix] = count of indices equal to current prefix
        ans = 0
        freq[0] = 1
        prefix_xor = 0
        for x in nums:
            prefix_xor ^= x
            ans += freq[prefix_xor]
            freq[prefix_xor] += 1
        return ans
            