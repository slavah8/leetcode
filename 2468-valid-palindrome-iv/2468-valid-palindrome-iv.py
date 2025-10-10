class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        if len(s) == 1 or len(s) == 2:
            return True
        
        left = 0
        right = len(s) - 1
        count = 0
        while left < right:
            if s[left] != s[right]:
                count += 1
            left += 1
            right -= 1
        
        if count == 1 or count == 2 or count == 0:
            return True
        else:
            return False