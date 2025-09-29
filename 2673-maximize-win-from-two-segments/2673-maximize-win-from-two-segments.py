class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        pos = prizePositions

        N = len(pos)

        best_left = [0] * N
        left = 0

        for right in range(N):

            while pos[right] - pos[left] > k: # need to shrink
                left += 1
            window = right - left + 1
            best_left[right] = window if right == 0 else max(best_left[right - 1], window)
        
        
        ans = 0
        left = 0
        for right in range(N):
            while pos[right] - pos[left] > k:
                left += 1
            length = right - left + 1
            if left > 0:
                ans = max(ans, length + best_left[left - 1])
            else:
                ans = max(ans, length)
        return ans