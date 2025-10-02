class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        pairs = sorted((intervals[i][0], i) for i in range(N)) # (start, idx)
        starts = [s for s, _ in pairs]

        ans = [-1] * N
        for i, (_, end_i) in enumerate(intervals):
            j = bisect_left(starts, end_i)
            if j < N:
                ans[i] = pairs[j][1]
        
        return ans