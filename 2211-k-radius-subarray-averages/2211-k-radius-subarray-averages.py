class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        N = len(nums)
        left = 0
        size = 2 * k + 1
        window_sum = 0
        result = [-1] * N
        for right in range(N):
            window_sum += nums[right]
            while right - left + 1 > size:
                window_sum -= nums[left]
                left += 1
            if right - left + 1 == size:
                center = left + k
                result[center] = window_sum // size

        return result
