class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        # We need max(chargeTimes[L..R]) quickly as the window moves
        # Keep a deque of indices, decreasing by chargeTimes
        # front is always the index of the max in the window

        dq = deque()
        run_sum = 0
        N = len(chargeTimes)
        L = 0
        best = 0
        
        for R in range(N):
            run_sum += runningCosts[R]
            while dq and chargeTimes[dq[-1]] <= chargeTimes[R]:
                dq.pop()

            dq.append(R)

            while dq and chargeTimes[dq[0]] + (R - L + 1) * run_sum > budget:
                if dq[0] == L:
                    dq.popleft()
                left_cost = runningCosts[L]
                run_sum -= left_cost
                L += 1
            
            best = max(best, R - L + 1)
        return best