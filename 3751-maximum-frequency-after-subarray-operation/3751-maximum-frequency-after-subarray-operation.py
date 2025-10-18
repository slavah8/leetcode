class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        

        total_k = sum(1 for x in nums if x == k)
        ans = total_k # do nothing answer

        N = len(nums)

        for v in range(1, 51):
            if v == k:
                continue
            
            best = 0
            max_gain = 0
            for x in nums:
                if x == v:
                    delta = 1
                elif x == k:
                    delta = -1
                else:
                    delta = 0
                best = max(0, best + delta)
                max_gain = max(max_gain, best)
            
            ans = max(ans, total_k + max_gain)
        return ans