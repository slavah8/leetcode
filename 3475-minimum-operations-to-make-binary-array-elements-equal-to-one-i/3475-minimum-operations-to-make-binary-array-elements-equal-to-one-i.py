class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        N = len(nums)
        need = [1] * N
        for i, x in enumerate(nums):
            if x == 0 and i + 2 < N:
                nums[i] = 1
                if i + 1 < N:
                    nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                if i + 2 < N:
                    nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                operations += 1
        if need != nums:
            return -1
        else:
            return operations
