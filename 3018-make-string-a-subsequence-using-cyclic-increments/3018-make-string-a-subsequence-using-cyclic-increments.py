class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        i = 0
        j = 0
        n = len(str1)
        m = len(str2)
        while i < n and j < m:
            char = str1[i]
            next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            print(next_char)
            if char == str2[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            elif next_char == str2[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            else:
                i += 1
        return False
            
