class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        INF = 10 ** 15
        self.ans = INF
        loads = [0] * k

        def dfs(i):
            # i is the index in jobs
            if i == len(jobs):
                self.ans = min(self.ans, max(loads))
                return
            
            if max(loads) > self.ans: # prune
                return
            
            time = jobs[i]
            seen_zero = False
            for l in range(k): # index in loads
                if loads[l] == 0 and seen_zero:
                    continue

                loads[l] += time
                if loads[l] < self.ans:
                    dfs(i + 1)
                loads[l] -= time

                if loads[l] == 0:
                    seen_zero = True
        dfs(0)
        return self.ans

                
