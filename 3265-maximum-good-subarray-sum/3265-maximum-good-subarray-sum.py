class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        seen = defaultdict(list) # val : indices
        n = len(nums)
        INF =  10 ** 15
        best = None
        prefix = 0
        # # min prefix sum seen so far for each value v
        min_pref = defaultdict(lambda : INF)
        
        for j, x in enumerate(nums):
            # |nums[i] - nums[j]| == k
            # nums[j] + k == nums[i]
            # nums[i] - nums[j] == -k
            # k - nums[j] = - nums[i]
            # nums[j] - k = nums[i] | nums[j] + k == nums[i]
            
            if min_pref[x + k] != INF:
                cand = (prefix + x) - min_pref[x + k]
                best = cand if best == None else max(best, cand)

            if min_pref[x - k] != INF:
                cand = (prefix + x) - min_pref[x - k]
                best = cand if best == None else max(best, cand)
            
            if prefix < min_pref[x]:
                min_pref[x] = prefix

            prefix += x
            
        return best if best else 0
