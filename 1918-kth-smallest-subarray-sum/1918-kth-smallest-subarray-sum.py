class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        
        
        n = len(nums)

        def count(limit):
            left = 0 
            total = 0
            curr_sum = 0
            for right in range(n):
                curr_sum += nums[right]
                while curr_sum > limit:
                    curr_sum -= nums[left]
                    left += 1
                total += (right - left + 1)
            return total

        low = min(nums)
        high = sum(nums)
        while low < high:
            mid = (low + high) // 2
            if count(mid) >= k:
                high = mid
            else:
                # if the count of sums doesnt reach k then 
                low = mid + 1
        return low


