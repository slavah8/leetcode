class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def longest_streak(arr):
            arr.sort()

            best = 1
            streak = 1
            for i in range(1, len(arr)):
                if arr[i - 1] + 1 == arr[i]:
                    streak += 1
                else:
                    streak = 1
                
                best = max(streak, best)
            
            return best
        
        h_streak = longest_streak(hBars)
        v_streak = longest_streak(vBars)
        
        side = min(h_streak + 1, v_streak + 1)
        return side * side