class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        N = len(nums)

        # how many numbers are missing up to index i 
        def missing(i):
            expected = nums[0] + i
            actual = nums[i]
            return actual - expected
        
        if missing(N - 1) < k:
            return nums[-1] + (k - missing(N - 1))

        # binary searching on indexes of nums
        # we want the first index such that missing(i) >= k
        # which means the kth num is in between nums[low - 1] and nums[low]
        low = 0
        high = N - 1

        while low < high:
            mid = (low + high) // 2

            if missing(mid) < k: # less missing numbers than k so answer has to be to the right
                low = mid + 1
            else:
                high = mid
        return nums[low - 1] + (k - missing(low - 1))
