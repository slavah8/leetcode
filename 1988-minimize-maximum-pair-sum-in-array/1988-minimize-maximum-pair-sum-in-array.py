class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)
        N = len(nums)
        l = 0
        r = N - 1
        pairs = []
        while l < r:
            pairs.append((nums[l], nums[r]))
            l += 1
            r -= 1
        INF = 10 ** 15
        ans = 0
        for p in pairs:
            summ = sum(p)
            if summ > ans:
                ans = summ
        return ans
