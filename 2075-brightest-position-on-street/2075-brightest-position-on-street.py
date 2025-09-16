class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = defaultdict(int)
        for pos, rng in lights:
            L = pos - rng
            R = pos + rng
            events[L] += 1
            events[R + 1] -= 1

        print(events)
        best = -1

        curr = 0
        ans = 0
        
        sorted_events = dict(sorted(events.items(), key = lambda x: x[0]))
        print(sorted_events)
        for x in sorted(events):
            curr += events[x]
            if curr > best:
                ans = x
                best = curr

        return ans




