class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        curr_end = -1

        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            start, end = interval

            if start < curr_end:
                return False
            else:
                curr_end = end
        
        return True