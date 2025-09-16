class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        delta = defaultdict(int)

        for L, R, color in segments:
            delta[L] += color
            delta[R] -= color

        prev = None
        running = 0
        ans = []
        for x in sorted(delta.keys()):
            if prev is not None and running > 0 and prev < x:
                ans.append((prev, x, running))
            prev = x
            running += delta[x]
        return ans