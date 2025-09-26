class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        median = nums[N // 2]
        print(median)
        total = 0
        for i in range(N):
            total += abs(median - nums[i])
        return total
