class Solution:
    def checkString(self, s: str) -> bool:
        
        first_b = -1
        last_a = -1
        for i, char in enumerate(s):
            if char == 'b':
                first_b = i
                break
        for i, char in enumerate(s):
            if char == 'a':
                last_a = i
        print(last_a)
        print(first_b)
        
        if last_a != -1 and first_b == -1:
            return True

        if last_a > first_b:
            return False
        if last_a < first_b:
            return True
        
        
        