class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
        # binary search on min cost path 
        # path costs the max jump
        N = len(stones)
        if N == 2:
            return stones[-1] - stones[0]
        # can the frog do a round trip without any any jump exceeding M?
        def can_go(M):
            for i in range(2, N):
                if stones[i] - stones[i - 2] > M:
                    return False
            return True


        low = 0
        high = stones[-1] - stones[0]

        while low < high:
            mid = (low + high) // 2
            if can_go(mid):
                high = mid
            else:
                low = mid + 1
        return low

