class Solution:
    def checkRecord(self, s: str) -> bool:
        
        absent = 0
        run = 0
        for ch in s:
            if ch == 'A':
                absent += 1
                run = 0
                if absent == 2:
                    return False
            elif ch == 'L':
                run += 1
                if run == 3:
                    return False
            else:
                run = 0
        
        return True

            
