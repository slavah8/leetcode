class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        # greedy invariant always increment the lowest number?
        heap = []
        for i, x in enumerate(nums):
            heapq.heappush(heap, (x, i))

        for _ in range(k):
            x, idx = heapq.heappop(heap)
            x = x + 1
            nums[idx] = x
            heapq.heappush(heap, (x, idx))
        print(nums)
        prod = 1
        for x in nums:
            prod = (prod * x) % MOD
        return prod