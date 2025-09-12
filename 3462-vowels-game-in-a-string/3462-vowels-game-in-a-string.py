class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        num_vowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for char in s:
            if char in vowels:
                num_vowels += 1
        
        if num_vowels == 0:
            return False

        if num_vowels % 2 == 1:
            return True
        
        if num_vowels % 2 == 0 and num_vowels > 0:
            return True
        

        
