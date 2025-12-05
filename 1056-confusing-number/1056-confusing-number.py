class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        rot_map = {0: 0, 1: 1, 6: 9, 8:8, 9: 6}
        digits = [0,1,6,8,9]
        def is_confusing(x):
            old = x
            rot = 0
            while x > 0:
                digit = x % 10
                if digit not in digits:
                    return False
                rot = rot * 10 + rot_map[digit]
                x = x // 10
            return old != rot
        
        return is_confusing(n)
