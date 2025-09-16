class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda p:p[1])
        print(points)

        arrow_x = points[0][1] # greedily place arrow at the endpoint
        # any start before this arrow is shot too
        arrows = 1
        for point in points[1:]:
            start = point[0]
            end = point[1]
            if start <= arrow_x:
                continue
            # need another arrow to shoot this interval
            # place arrow_x at the endpoint again and repeat
            arrows += 1
            arrow_x = end
        return arrows
