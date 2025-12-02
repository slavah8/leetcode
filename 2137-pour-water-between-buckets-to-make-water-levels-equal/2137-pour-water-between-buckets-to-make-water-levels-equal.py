class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        n = len(buckets)
        eff = 1.0 - loss / 100.0
        # is it possible to make every bucket x 


        def can(x):
            surplus = 0.0
            deficit = 0.0
            for b in buckets:
                if b > x:
                    surplus += (b - x)
                else:
                    deficit += (x - b)

            return surplus * eff >= deficit
        
        low = 0.0
        high = max(buckets)
        for _ in range(60):
            mid = (low + high) / 2
            if can(mid):
                low = mid
            else:
                high = mid
        return low
            

            

