class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        first_letter = word[0]
        if len(word) == 1:
            return True

        if first_letter.isupper():
            # all chars need to caps 
            # or the rest have to be lowercase
            lower_case = False
            second_letter = word[1]
            if second_letter.islower():
                lower_case = True
            
            for ch in word[2:]:
                if lower_case and ch.isupper():
                    return False
                
                if not lower_case and ch.islower():
                    return False
            
            return True
        else:
            # all chars need to lowercase
            for ch in word[1:]:
                if ch.isupper():
                    return False
            
            return True
            
                
