class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0

        nums.sort()
        print(nums)
        N = len(nums)
        for i in range(N):
            left = i + 1
            right = N - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ < target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
        return count
            