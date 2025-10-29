class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        
        print(prefix)

        count = prefix.count(0)
        return count - 1