class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        x = int(num)
        rotated = 0
        rotate_map = {0: 0, 1: 1, 6: 9, 8:8, 9:6}
        valid = [0,1,6,8,9]
        while x > 0:
            digit = x % 10
            if digit not in valid:
                return False
            rotated = rotated * 10 + rotate_map[digit]
            x = x // 10
        
        return int(num) == rotated
            