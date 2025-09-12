class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        left = 0
        prefix = 0
        count = 0
        for right in range(N):
            num = nums[right]
            prefix += num
            length = right - left + 1
            while left < N and length * prefix >= k: # need to shrink window
                num_left = nums[left]
                prefix -= num_left
                length -= 1
                left += 1
            count += length
        return count
            