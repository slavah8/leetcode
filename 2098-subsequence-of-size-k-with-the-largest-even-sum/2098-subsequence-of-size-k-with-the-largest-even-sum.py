class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse = True)

        chosen = nums[:k]
        rest = nums[k:]

        s = sum(nums[:k])

        if s % 2 == 0:
            return s

        
        INF = 10 ** 15

        min_odd = INF
        min_even = INF

        for i in range(k):

            if nums[i] % 2 == 0:
                min_even = min(nums[i], min_even)
            else:
                min_odd = min(nums[i], min_odd)
        
        # If sum is odd, we must flip parity

        max_odd = -1
        max_even = -1

        for x in rest:
            if x % 2 == 0:
                max_even = max(max_even, x)
            else:
                max_odd = max(max_odd, x)
        
        best = -1

        if min_odd != INF and max_even != -1:
            # makes it even but we need to check if there is an even in rest
            best = max(best, s - min_odd + max_even)
        
        if min_even != INF and max_odd != -1:
            best = max(best, s - min_even + max_odd)
        
        return best
        



