class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        S = sum(nums)
        if S % k == 0:
            return 0
        
        return S % k