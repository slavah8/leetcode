class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # is it possible for the robber to steal less than this amount C
        def can(C):
            i = 0
            take = 0
            while i < N:
                if nums[i] <= C:
                    take += 1
                    i += 2
                else:
                    i += 1
            return take >= k
        
        low = min(nums)
        high = max(nums)
        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        return low
