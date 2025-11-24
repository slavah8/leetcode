class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        ans = []
        n = len(nums)
        for bit in nums:
            curr = (curr << 1) + bit
            ans.append(curr % 5 == 0)
        return ans
            