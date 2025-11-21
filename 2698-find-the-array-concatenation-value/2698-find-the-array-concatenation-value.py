class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        value = 0
        while nums:
            if len(nums) >= 2:
                x = nums[0]
                y = nums[-1]
                len_y = len(str(y))
                nums = nums[1:-1]
                concat = 1
                for _ in range(len_y):
                    concat *= 10
                concat *= x
                concat += y
                value += concat
            else:
                x = nums[0]
                value += x
                nums = nums[1:]
        return value
