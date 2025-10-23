class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        S = sum(nums)
        N = len(nums)
        target = S - x
        # we are looking for longest subarray with target = S - x

        if S == x:
            return len(nums)
        
        if S < x:
            return -1
        
        l = 0
        curr_sum = 0
        best = -1 # longest subarray equal to target
        for r, x in enumerate(nums):
            curr_sum += x

            while curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            
            if curr_sum == target:
                best = max(best, r - l + 1)
        return N - best if best != -1 else -1
            
