class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)

        N = len(nums)

        s = 0
        while s + 1 < N and nums[s] <= nums[s + 1]:
            s += 1
        
        if s == N - 1:
            return 0
        
        e = N - 1
        while e - 1 >= 0 and nums[e] >= nums[e - 1]:
            e -= 1
        
        mid_min = min(nums[s:e + 1])
        mid_max = max(nums[s:e + 1])
        
        while s > 0 and nums[s - 1] > mid_min:
            s -= 1
        
        while e + 1 < N and nums[e + 1] < mid_max:
            e += 1
        return e - s + 1