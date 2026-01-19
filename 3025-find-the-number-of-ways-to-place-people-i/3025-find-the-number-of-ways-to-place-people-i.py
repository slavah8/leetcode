class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        n = len(points)

        points.sort(key = lambda x: (x[0], -x[1])) # sort by left
        count = 0

        for i in range(n):

            x1, y1 = points[i]
            for j in range(i + 1, n):

                x2, y2 = points[j]
                
                if y1 < y2:
                    continue
                
                # A is upper left side of B
            
                valid = True
                for x, y in points:
                    if (x, y) == (x1, y1) or (x, y) == (x2, y2):
                        continue
                    
                    if x1 <= x <= x2 and y2 <= y <= y1:
                        valid = False
                        break
                
                if valid:
                    count += 1
        return count
                    
                    



                
