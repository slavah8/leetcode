class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        
        jobs.sort()
        workers.sort()
        days = 0
        n = len(jobs)
        print(jobs)
        print(workers)
        for i in range(n):
            days = max(days, math.ceil(jobs[i] / workers[i]))
        return days
        



