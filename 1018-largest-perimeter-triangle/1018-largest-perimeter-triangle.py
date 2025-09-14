class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)

        best = 0
        N = len(nums)
        for i in range(N):
            if i + 2 < N and nums[i] < nums[i + 1] + nums[i + 2]:
                best = nums[i] + nums[i + 1] + nums[i + 2]
                break
        
        return best