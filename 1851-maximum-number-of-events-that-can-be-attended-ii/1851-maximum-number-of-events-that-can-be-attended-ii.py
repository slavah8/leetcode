class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort(key=lambda x: x[0])

        N = len(events)
        starts = [s for s,_,_ in events]
        ends = [e for _,e,_ in events]
        vals = [v for _,_, v in events]

        # next index (first start > end_i)
        next_idx = [0] * N

        for i in range(N):
            next_idx[i] = bisect.bisect_right(starts, ends[i]) # first start greater than some end
        
        # dp[t][i] = the maximum total value obtainable from the subarray of events i..n-1, if you can attend at most t events.

        dp = [[0] * (N + 1) for _ in range(k + 1)]
        for t in range(1, k + 1):
            for i in range(N - 1, -1, -1):
                # use this event or dont
                skip = dp[t][i + 1]
                take = vals[i] + dp[t - 1][next_idx[i]]
                dp[t][i] = max(skip, take)
        return dp[k][0]