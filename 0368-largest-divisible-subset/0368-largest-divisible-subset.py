class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        # dp[i] = length of the largest divisible subset (chain) that ends at index i
        # parent[i] = previous index in the chain
        nums.sort()
        n = len(nums)
        dp = [1] * n 
        parent = [-1] * n
        best_end = -1
        best_len = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
        
            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i
        
        res = []
        cur = best_end
        while cur != -1:
            res.append(nums[cur])
            cur = parent[cur]
        
        res.reverse()
        return res
        

                    

