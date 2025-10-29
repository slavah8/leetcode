class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        
        print(pref)

        minn = min(pref)
        # startValue - minn >= 1
        # x >= 1 + minn
        
        x = -minn + 1
        return x