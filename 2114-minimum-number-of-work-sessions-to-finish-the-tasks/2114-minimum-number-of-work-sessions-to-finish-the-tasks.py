class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse = True)
        # mask = which tasks are completed so far
        # remain = time left in the current section
        n = len(tasks)
        FULL = (1 << n) - 1
        # dfs(mask, remain) = minimum number of sessions needed to finish remaining tasks, 
        # given remain left in the current session
        INF = 10 ** 15
        @lru_cache(None)
        def dfs(mask, remain):
            if mask == FULL:
                # if no task placed in current session (remain == sessionTime), no session to count
                return 0 if remain == sessionTime else 1
            
            tried = set()
            best = INF
            for i in range(n):
                if (mask >> i) & 1 == 1: # already completed task i
                    continue 
                if remain >= tasks[i]:
                    best = min(best, dfs(mask | (1 << i), remain - tasks[i]))
                else:
                    # start new session
                    if remain == sessionTime and tasks[i] in tried:
                        continue
                    best = min(best, dfs(mask, sessionTime) + 1)
            return best

                
        return dfs(0, sessionTime)