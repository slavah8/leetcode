class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        ages.sort()

        n = len(ages)
        ans = 0
        for i, age in enumerate(ages):
            if age <= 14:
                continue
            min_y = 0.5 * age + 7
            
            L = bisect_right(ages, min_y)
            R = bisect_right(ages, age) - 1
            if L <= R:
                ans += (R - L)
        return ans

