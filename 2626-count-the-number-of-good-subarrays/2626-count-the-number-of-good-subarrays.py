class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        num_freqs = collections.defaultdict(int)
        ans = 0
        pairs = 0
        l = 0
        for r, x in enumerate(nums):
            pairs += num_freqs[x]
            num_freqs[x] += 1
            while pairs >= k:
                ans += (n - r)
                left_num = nums[l] 
                num_freqs[left_num] -= 1
                pairs -= num_freqs[left_num]
                l += 1
            
            
        return ans
            

