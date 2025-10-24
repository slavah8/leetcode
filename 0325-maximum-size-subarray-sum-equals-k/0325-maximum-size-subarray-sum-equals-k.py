class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        first = {0: 0}        # prefix sum -> earliest index (1-based length position)

        
        best = 0
        # prefix[r + 1] - prefix[l] = k -> prefix[l] = prefix[r + 1] - k
        prefix = 0
        for r, x in enumerate(nums, 1):
            prefix += x

            if prefix - k in first:
                cand = r - first[prefix - k]
                if cand > best:
                    best = cand
            if prefix not in first:
                first[prefix] = r
        return best


