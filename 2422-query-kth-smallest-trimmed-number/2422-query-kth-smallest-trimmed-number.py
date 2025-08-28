class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        M = len(nums[0])

        order = list(range(N))
        def counting_sort(order, pos):
            count = [0] * 10
            for idx in order:
                d = ord(nums[idx][pos]) - ord('0')
                count[d] += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            out = [0] * N
            for i in range(N - 1, -1, -1):
                idx = order[i]
                d = ord(nums[idx][pos]) - ord('0')
                count[d] -= 1
                out[count[d]] = idx
            return out
        
        order_by_len = [None] * (M + 1)

        for pos in range(M - 1, -1, -1):
            order = counting_sort(order, pos)
            L = M - pos
            order_by_len[L] = order[:]
        
        ans = []
        for k, trim in queries:
            ans.append(order_by_len[trim][k - 1])
        
        return ans