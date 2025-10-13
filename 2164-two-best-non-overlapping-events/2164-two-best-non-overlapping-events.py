class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        ev = sorted(events, key = lambda x: x[1]) # sort by ends
        print(ev)
        ends = [e for _, e, _ in ev]
        values = [v for _, _, v in ev]

        # best single event value up to each end
        prefix = [] #
        mx = 0
        for v in values:
            mx = max(mx, v)
            prefix.append(mx)
        print(prefix)
        ans = -1
        # for each event as the "later" one find best event before this one starts
        for s, e, val in events:
            p = bisect.bisect_left(ends, s) - 1
            best_earlier = prefix[p] if p >= 0 else 0
            ans = max(ans, best_earlier + val)
        return ans
            

