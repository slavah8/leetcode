class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        counts = collections.Counter(nums)

        count = counts[target]
        N = len(nums)
        return count > N / 2