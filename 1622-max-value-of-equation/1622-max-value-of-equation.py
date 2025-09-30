class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        ∣xi​−xj​∣ = xj​−xi​
        yi + yj + xj - xi = (yj + xj) + (yi - xi)
        we want the best (yi - xi) for a fixed j with
        xj - xi <= k -> xi >= xj - k

        """
        dq = deque() # (xi, val)
        INF = 10 ** 20
        best = -INF
        for xj, yj in points:
            while dq and xj - dq[0][0] > k:
                dq.popleft()

            if dq:
                best = max(best, (yj + xj) + (dq[0][1]))
            
            val = yj - xj
            while dq and dq[-1][1] < val:
                dq.pop()
            dq.append((xj, val))
        return best

            


