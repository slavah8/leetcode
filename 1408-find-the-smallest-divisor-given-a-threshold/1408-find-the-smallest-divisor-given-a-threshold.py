class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        summ = sum(nums)
        low = 1
        high = summ
        # is the sum less than or equal to the threshold
        def under_threshold(div):
            summ = 0
            for x in nums:
                summ += math.ceil(x / div)
            return summ <= threshold

            
        # do binary search on divisors?


        while low < high:
            mid = (low + high) // 2

            if under_threshold(mid):
                high = mid
            else:
                low = mid + 1
        return low


