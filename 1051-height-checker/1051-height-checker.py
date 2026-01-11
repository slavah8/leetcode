class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sorted_heights = sorted(heights)

        i = 0
        j = 0
        n = len(heights)
        count = 0
        while i < n and j < n:
            if heights[i] != sorted_heights[j]:
                count += 1
            i += 1
            j += 1
        
        return count

