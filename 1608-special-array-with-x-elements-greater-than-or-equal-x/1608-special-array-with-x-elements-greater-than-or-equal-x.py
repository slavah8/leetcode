class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        low = 0
        high = 1000
        def check(x):
            count = 0
            for i in range(n):
                if nums[i] >= x:
                    count = n - i
                    break
            return count == x


        for x in range(1000):
            if check(x):
                return x
        
        return -1