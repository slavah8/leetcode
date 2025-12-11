class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        best = 0
        n = len(img1)
        # try to shift img1 and see how many 1s overlap in img2
        for dr in range(-(n - 1), n):
            for dc in range(-(n - 1), n):
                overlap = 0

                for r in range(n):
                    for c in range(n):
                        r2 = r + dr
                        c2 = c + dc
                        if 0 <= r2 < n and 0 <= c2 < n:
                            if img1[r][c] == 1 and img2[r2][c2] == 1:
                                overlap += 1
                        
                best = max(best, overlap)
        return best
