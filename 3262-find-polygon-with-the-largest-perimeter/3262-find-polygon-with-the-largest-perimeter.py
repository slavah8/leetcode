class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        best = -1

        nums.sort()
        print(nums)
        summ = 0
        N = len(nums)
        ans = -1
        for i in range(N):
            longest_side = nums[i]
            summ += longest_side
            if summ - longest_side > longest_side:
                ans = max(ans, summ)
        
        return ans


            