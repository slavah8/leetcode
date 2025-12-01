class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        
        n = len(points)

        dist = [0] * n

        for i, (x, y) in enumerate(points):
            dist[i] = max(abs(x), abs(y))
        
        tag_to_dist = defaultdict(list)

        for i, ch in enumerate(s):
            tag_to_dist[ch].append(dist[i])
        
        INF = 10 ** 10
        banned_radius = INF

        for ch, arr in tag_to_dist.items():
            if len(arr) >= 2:
                arr.sort()
                second = arr[1]
                if second < banned_radius:
                    banned_radius = second
        
        if banned_radius == INF:
            return n
        
        pts = 0
        for d in dist:
            if d < banned_radius:
                pts += 1
        
        return pts
            