class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        
        n = len(strength)
        INF = 10 ** 15
        best = INF
        order = sorted(range(n), key = lambda i: strength[i], reverse = True)
        used = [False] * n
        
        def backtrack(time_so_far, t):
            # t how many locks broken
            nonlocal best
            if time_so_far >= best: # prune early
                return

            if t == n:
                best = min(best, time_so_far)
                return
            
            x = 1 + t * k
            for idx in order:
                if not used[idx]:
                    used[idx] = True
                    # time needed to break this lock with the current factor x
                    add = math.ceil(strength[idx] / x)
                    backtrack(time_so_far + add, t + 1)
                    used[idx] = False
        backtrack(0, 0)
        return best
            
            

            

