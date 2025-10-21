class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        # PLE[i] = index of Previous Less element to the left of i
        # NLE[i] = index of Next Less-or-Equal element to the right of i

        # compute PLE
        PLE = [-1] * N
        stack = [] # increasing stack
        for i, x in enumerate(arr):
            while stack and x <= arr[stack[-1]]:
                k = stack.pop()
            PLE[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # compute NLE
        stack.clear()

        NLE = [N] * N
        for i, x in enumerate(arr):

            while stack and x < arr[stack[-1]] or (stack and arr[stack[-1]] == x):
                k = stack.pop()
                NLE[k] = i
            stack.append(i)

        ans = 0

        for i, x in enumerate(arr):
            left = i - PLE[i]
            right = NLE[i] - i
            ans = (ans + x * left * right) % MOD
        return ans

