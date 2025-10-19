class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        S = sum(nums)
        target = S / k
        if S % k != 0:
            return False

        nums.sort(reverse = True)  

        for x in nums:
            if x > target:
                return False
            
        bucket = [0] * k
        
        def dfs(i):
            if i == len(nums): # all numbers placed
                return True
            
            x = nums[i]
            for b in range(k):
                if bucket[b] + x > target:
                    continue
                
                bucket[b] += x
                if dfs(i + 1):
                    return True
                bucket[b] -= x
                if bucket[b] == 0:
                    break
            return False
        return dfs(0)

