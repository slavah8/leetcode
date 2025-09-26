class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        maxx = 0
        counts = defaultdict(int)
        left = 0
        summ = 0
        window_size = 0
        for right, x in enumerate(nums):
            summ += x
            counts[x] += 1
            window_size += 1
            while counts[x] > 1 or window_size > k:
                left_num = nums[left]
                counts[left_num] -= 1
                summ -= left_num
                window_size -= 1
                left += 1
            if window_size == k:
                maxx = max(maxx, summ)
        return maxx
