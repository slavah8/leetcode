class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, x in enumerate(nums):
            if x == 1:
                if last is not None and i - last - 1 < k:
                    return False
                last = i
        return True
