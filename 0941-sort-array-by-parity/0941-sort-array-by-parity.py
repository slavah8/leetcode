class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        N = len(nums)
        right = N - 1
        result = [-1] * N
        
        for x in nums:
            if x % 2 == 0: # even move to front
                result[left] = x
                left += 1
            else:
                result[right] = x
                right -= 1
        return result

