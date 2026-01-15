class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ended_segment = False
        started_segment = False
        for ch in s:
            
            if ch == '1' and not started_segment:
                started_segment = True
            
            if ch == '1' and ended_segment:
                return False
            
            if ch == '0' and started_segment:
                ended_segment = True
        
        return True
        