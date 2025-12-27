class Solution:
    def compressedString(self, word: str) -> str:
        

        n = len(word)

        comp = ""

        i = 0
        first_char = word[i]
        cur_length = 0
        while i < n:
            j = i
            while j < n and first_char == word[j] and cur_length < 9:
                cur_length += 1
                j += 1
            
            comp += str(cur_length) + first_char
            i = j
            first_char = word[i] if i < n else ""
            cur_length = 0
        
        return comp


