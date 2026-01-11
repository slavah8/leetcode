"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        intervals = []
        for emp in schedule:
            for inv in emp:
                intervals.append(inv)
        

        intervals.sort(key = lambda x: x.start)

        cur_end = intervals[0].end
        res = []

        for i in range(1, len(intervals)):

            start = intervals[i].start
            end = intervals[i].end

            if start > cur_end:
                # free time
                res.append(Interval(cur_end, start))
                cur_end = end
            else:
                cur_end = max(cur_end, end)

        return res