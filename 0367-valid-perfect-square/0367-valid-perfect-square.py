class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left = 1
        right = num // 2 + 1

        while left <= right:
            mid = (left + right) // 2
            square = (mid * mid)
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        
        return False