class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        answer = []

        def inside(px, py, x, y, r):

            dx = px - x
            dy = py - y
            return dx * dx + dy * dy <= r * r
            
        for q in queries:
            x, y, r = q
            
            count = 0

            for p in points:
                px, py = p
                if inside(px, py, x, y, r):
                    count += 1
            
            answer.append(count)
        
        return answer

