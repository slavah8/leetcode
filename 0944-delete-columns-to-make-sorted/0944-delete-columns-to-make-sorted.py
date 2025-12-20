class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        count = 0
        for c in range(cols):
            curr_string = strs[0][c]
            for r in range(1, rows):
                if curr_string > strs[r][c]:
                    count += 1
                    break
                curr_string = strs[r][c]
        
        return count
