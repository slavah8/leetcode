class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        

        nums.sort()
        n = len(nums)

        i = 0
        j = 1
        count = 0
        if k == 0:
            i = 1
            while i < n:
                if nums[i - 1] == nums[i]:
                    count += 1
                    val = nums[i]
                    while i < n and nums[i] == val:
                        i += 1
                else:
                    i += 1
            return count
        
        while i < n and j < n:
            diff = nums[j] - nums[i]

            if diff == k:
                count += 1
                val_i = nums[i]
                while i < n and nums[i] == val_i:
                    i += 1
                
                val_j = nums[j]
                while j < n and nums[j] == val_j:
                    j += 1
                
                if j <= i:
                    j = i + 1
            elif diff < k:
                j += 1
            else:
                i += 1
        return count
