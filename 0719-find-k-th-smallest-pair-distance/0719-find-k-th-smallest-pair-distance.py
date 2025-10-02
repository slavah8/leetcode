class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        # It counts how many pairs (i, j) with i < j have distance ≤ D.
        nums.sort()
        def count_leq(D):
            left = 0
            N = len(nums)
            cnt = 0
            for right in range(N):
                while nums[right] - nums[left] > D:
                    left += 1
                cnt += right - left
            return cnt
        
        # binary search on possible distances
        low = 0
        high = nums[-1] - nums[0] # biggest pos distance in the arr
        while low < high:
            mid = (low + high) // 2
            if count_leq(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return high

                