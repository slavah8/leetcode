class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        N = len(nums)
        PLE = [-1] * N
        NLE = [N] * N
        stack = []
        MOD = 10 ** 9 + 7
        for i, x in enumerate(nums):
            while stack and x <= nums[stack[-1]]:
                stack.pop()
            PLE[i] = stack[-1] if stack else -1
            stack.append(i)
        print(PLE)
        stack.clear()
        for i, x in enumerate(nums):
            while stack and x <= nums[stack[-1]]:
                k = stack.pop()
                NLE[k] = i
            stack.append(i)
        
        print(NLE)

        prefix = [0] * (N + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        print(prefix)

        ans = 0
        for i, x in enumerate(nums):
            l = PLE[i] + 1
            r = NLE[i] - 1
            summ = prefix[r + 1] - prefix[l]
            product = x * summ
            ans = max(ans, product)
        return ans % MOD
