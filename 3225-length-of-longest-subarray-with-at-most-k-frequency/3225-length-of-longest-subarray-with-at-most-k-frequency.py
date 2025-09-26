class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        left = 0
        N = len(nums)
        counts = defaultdict(int)
        longest = 0
        for right in range(N):
            right_num = nums[right]
            counts[right_num] += 1
            while counts[right_num] > k:
                left_num = nums[left]
                counts[left_num] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest
