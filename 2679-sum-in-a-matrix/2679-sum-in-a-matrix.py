class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = len(nums)
        cols = len(nums[0])
        score = 0
        for _ in range(cols):
            global_max = 0
            for r, row in enumerate(nums):
                local_max = 0
                for c, x in enumerate(row):
                    
                    if x > global_max:
                        global_max = x
                    
                    if x > local_max:
                        local_max = x
                if local_max != 0:
                    row.remove(local_max)
                nums[r] = row
            score += global_max

        return score

