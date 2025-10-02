class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        INF = 10 ** 20
        heaters.sort()
        ans = 0

        for h in houses:
            j = bisect.bisect_left(heaters, h)
            left = h - heaters[j - 1] if j > 0 else INF
            right = heaters[j] - h if j < len(heaters) else INF
            ans = max(ans, min(left, right))
        
        return ans