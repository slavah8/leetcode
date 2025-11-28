class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
      

            INF = 10 ** 10
            n = len(nums)
            if n == 0:
                return 0
            max_left = [0] * n
            max_left[0] = nums[0]
            for i in range(1, n):
                max_left[i] = max(max_left[i - 1], nums[i])
            
            min_right = [0] * n
            min_right[n - 1] = nums[n - 1]
            for i in range(n - 2, -1, -1):
                min_right[i] = min(min_right[i + 1], nums[i])

            count = 0
            for i in range(n):
                 # Is this specific value guaranteed to be found
                x = nums[i]
                left_max = max_left[i - 1] if i - 1 >= 0 else -INF
                right_min = min_right[i + 1] if i + 1 < n else INF
                # check if it gets deleted by some value to its left
                # check if it gets deleted by some value to its right

                # if left_max > x or right_min < x then it gets deleted
                if left_max < x and right_min > x:
                    count += 1

            return count
