class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        i = 0
        j = len(nums) - 1
        INF = 10 ** 10
        best = -1
        while i < j:
            x, y = nums[i], nums[j]
            summ = x + y
            if summ >= k: # shift right
                j -= 1
            else:
                best = max(best, summ)
                i += 1
        return best

