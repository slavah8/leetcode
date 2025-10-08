class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        # tails[k] = the smallest possible ending height of any non-decreasing subsequence of length k+1 seen so far.
        # increasing array
        tails = []
        result = []
        for h in obstacles:
            pos = bisect.bisect_right(tails, h)
            
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
            result.append(pos + 1)
        return result

