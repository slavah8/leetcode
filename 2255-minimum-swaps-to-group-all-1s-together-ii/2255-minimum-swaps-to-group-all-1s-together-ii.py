class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = 0
        if nums == [0]:
            return 0
        for x in nums:
            if x == 1:
                ones += 1
            
        arr = nums + nums
        N = len(nums)
        zeroes_in_window = 0
        ans = N
        left = 0
        for right in range(2 * N):
            if arr[right] == 0:
                zeroes_in_window += 1

            while right - left + 1 > ones:
                left_num = arr[left]
                if left_num == 0:
                    zeroes_in_window -= 1
                left += 1
            
            if right - left + 1 == ones and left < N:
                ans = min(ans, zeroes_in_window)

            if left >= N:
                break
        return ans
            
