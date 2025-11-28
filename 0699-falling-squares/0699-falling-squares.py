class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        
        n = len(positions)
        intervals = []
        maxx = 0
        ans = []
        for left, side in positions:
            right = left + side
            base_height = 0
            for L2, R2, H2 in intervals:
                if left < R2 and right > L2:
                    base_height = max(base_height, H2)
            curr_height = base_height + side
            
            intervals.append((left, right, curr_height))
            maxx = max(maxx, curr_height)
            ans.append(maxx)
        return ans

