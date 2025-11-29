class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        MAX_H = 100

        # buckets[h] = sorted list of lengths li of rectangles with height exactly h

        buckets = [[] for _ in range(MAX_H + 1)]
        for length, height in rectangles:
            buckets[height].append(length)
        
        for h in range(1, 101):
            buckets[h].sort()

        res = [0] * len(points)
        for idx, (x, y) in enumerate(points):
            cnt = 0
            for h in range(y, MAX_H + 1):
                arr = buckets[h]
                if not arr:
                    continue
                i = bisect_left(arr, x)
                cnt += (len(arr) - i)
            res[idx] = cnt
        return res

                

                
