class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
       
        N = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        starts = [s for s, _, _ in jobs]
        ends = [e for _, e, _ in jobs]
        vals = [v for _, _, v in jobs]

        # dp[i] = best profit using first i jobs
        dp = [0] * (N + 1)

        for i in range(1, N + 1):
            s, e, v = jobs[i - 1]

            # skip this job or use it
            skip = dp[i - 1]
            # if we take this job then take the best profit using all jobs that ended before this started
            p = bisect.bisect_right(ends, s) - 1
            take = v + (dp[p + 1] if p >= 0 else 0)
            dp[i] = max(skip, take)
        return dp[N]

        
