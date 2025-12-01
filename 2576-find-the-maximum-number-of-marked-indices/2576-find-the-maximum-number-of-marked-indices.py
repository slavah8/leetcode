class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        def can(k):
            if k == 0:
                return True
            if k * 2 > n:
                return False
            
            for i in range(k):
                if nums[i] * 2 > nums[n - k + i]:
                    return False
            return True
        
        low = 0
        high = n // 2
        best = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best * 2

        