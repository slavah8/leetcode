class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * 102

        for L, R in nums:
            diff[L] += 1
            diff[R + 1] -= 1
        
        prefix = [0] * 103

        for i, x in enumerate(diff):
            prefix[i + 1] = prefix[i] + x
        
        total = 0
        for x in prefix:
            if x > 0:
                total += 1
        return total

