class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        

        n = len(nums)
        INF = 10 ** 10
        best = INF
        for i in range(n):
            for j in range(i, n):
                sub = nums[i:j + 1]
                print(sub)
                bit_sum = 0
                for x in sub:
                    bit_sum |= x
                
                if bit_sum >= k:
                    best = min(best, len(sub))
        
        return best if best != INF else -1

