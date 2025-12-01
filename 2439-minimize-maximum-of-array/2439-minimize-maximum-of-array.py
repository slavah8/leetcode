class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        n = len(nums)

        
        # can we reduce every num to at least num
        def can(num):
            
            arr = nums[:]
            n = len(arr)
            
            for i in range(n - 1, 0, -1):
                if arr[i] > num:
                    excess = arr[i] - num
                    arr[i - 1] += excess
                    arr[i] -= excess
            return arr[0] <= num
                

        low = 1
        high = max(nums)        
        ans = high
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if can(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
