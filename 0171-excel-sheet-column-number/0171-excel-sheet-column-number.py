class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            ans *= 26
            ans += ord(char) - ord('A') + 1
        
        return ans