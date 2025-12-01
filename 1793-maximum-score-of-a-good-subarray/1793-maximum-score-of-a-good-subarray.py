class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        l = r = k
        cur_min = nums[k]
        best = cur_min

        while l > 0 or r < n - 1:
            if l == 0:
                r += 1
                cur_min = min(cur_min, nums[r])
            elif r == n - 1:
                l -= 1
                cur_min = min(cur_min, nums[l])
            else:
                if nums[l - 1] >= nums[r + 1]:
                    l -= 1
                    cur_min = min(cur_min, nums[l])
                else:
                    r += 1
                    cur_min = min(cur_min, nums[r])
            
            best = max(best, cur_min * (r - l + 1))
        return best