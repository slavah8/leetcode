class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        
        n = len(nums)

        # dp defined as number of even subarrays up to ith index
        dp = [0] * (n + 1)
        ans = 0

        last_even = -1
        for i in range(n):

            x = nums[i]
            if x % 2 == 0:
                last_even = i
                ans += i + 1
            else:
                if last_even != -1:
                    ans += last_even + 1
            

        
        return ans
