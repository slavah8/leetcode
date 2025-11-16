class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        offset = 0
        n = len(columnTitle)

        for i in range(n):
            offset += 26 ** i
        
        ans = 0
        for char in columnTitle:
            ans *= 26
            ans += ord(char) - ord('A')
            
        
        return ans + offset


        