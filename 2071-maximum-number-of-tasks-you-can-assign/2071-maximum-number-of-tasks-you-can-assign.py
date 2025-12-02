class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n = len(tasks)
        m = len(workers)
        def can(t):
            pills_left = pills
            # start with the hardest task
            pool = workers[m - t: ][:]
            for i in range(t - 1, -1, -1):
                need = tasks[i]

                idx = bisect_left(pool, need)
                if idx < len(pool):
                    pool.pop(idx)
                    continue
                
                # need pill
                if pills_left == 0:
                    return False
                # w >= need - strength
                limit = need - strength
                idx = bisect_left(pool, limit)
                if idx == len(pool):
                    return False
                
                pills_left -= 1
                pool.pop(idx)
            return True


            
        lo = 0
        hi = min(n, m)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
                


