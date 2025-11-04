class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        print(prefix)

        if all(x >= 0 for x in prefix):
            return 0

        pref = 0
        heap = []
        ops = 0
        end = n - 1
        for i, x in enumerate(nums):
            pref += x
            heapq.heappush(heap, x)
            if pref < 0:
                minn = heapq.heappop(heap)
                nums.append(minn)
                pref -= minn
                ops += 1
        return ops
                


                

        
