class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        ans = [0] * n

        seen = collections.defaultdict(list) # value : idxs

        for i, x in enumerate(nums):
            seen[x].append(i)
        
        for val, idxs in seen.items():

            m = len(idxs)
            if m == 1:
                continue
            
            prefix = [0] * m
            prefix[0] = idxs[0]
            for t in range(1, m):
                prefix[t] = prefix[t - 1] + idxs[t]
            
            total_sum = prefix[-1]
            for k, x in enumerate(idxs):
                left = x * k - prefix[k - 1] if k > 0 else 0

                right_sum = total_sum - prefix[k] # # sum of indices strictly to the right of x:
                right_cnt = m - k - 1 # how many elements are to the RIGHT of x
                right = right_sum - x * right_cnt
                ans[x] = left + right
        return ans