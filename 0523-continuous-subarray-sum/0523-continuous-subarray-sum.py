class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        seen = {0: -1} # rem : idx

        rem = 0
        for i, x in enumerate(nums):
            rem = (rem + x) % k
            if rem in seen:
                if i - seen[rem] >= 2:
                    return True

            if rem not in seen:
                seen[rem] = i
        return False

