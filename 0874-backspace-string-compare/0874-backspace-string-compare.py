class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        text1 = ""
        text2 = ""

        for char in s:
            if char.isalpha():
                text1 += char
            else:
                text1 = text1[:-1]
        print(text1)

        for char in t:
            if char.isalpha():
                text2 += char
            else:
                text2 = text2[:-1]

        return text1 == text2