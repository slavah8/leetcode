class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        P = [0] * (n + 1)
        for i in range(1, n + 1):
            P[i] = P[i - 1] + nums[i - 1]
        
        ans = n + 1
        D = deque() # # Deque of indices of P, kept with increasing P[index]

        # we want shortest subarray so we keep deque of l index
        
        for r in range(n + 1):
            while D and (P[r] - P[D[0]]) >= k:
                ans = min(ans, r - D[0])
                D.popleft()
            
            # pop from the back
            while D and P[r] <= P[D[-1]]:
                D.pop()
            
            D.append(r)
        return ans if ans != n + 1 else -1

