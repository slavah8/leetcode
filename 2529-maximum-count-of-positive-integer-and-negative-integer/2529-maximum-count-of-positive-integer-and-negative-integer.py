class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        pos = 0
        neg = 0
        for i, x in enumerate(nums):
            if x > 0:
                pos += 1
            elif x < 0:
                neg += 1
        return max(pos, neg)