class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n = len(s)
        curr = s
        if curr == goal:
            return True

        def rotate(s):
            new_s = [""] * (n)
            for i in range(n - 1):
                new_s[i + 1] = s[i]
            new_s[0] = s[n - 1]
            return ''.join(new_s)
            
        for i in range(n):
            curr = rotate(list(curr))
            if curr == goal:
                return True
        
        return False