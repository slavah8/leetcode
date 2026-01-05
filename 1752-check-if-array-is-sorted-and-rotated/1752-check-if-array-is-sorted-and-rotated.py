class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        sorted_arr = sorted(nums)

        for x in range(0, n):
            # try rotating by i and check if its sorted_arr
            new_arr = [0] * n

            for i in range(0, n):
                new_arr[(i + x) % n] = nums[i]
            
            if new_arr == sorted_arr:
                return True
        
        return False
