class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        rows = len(mat)
        cols = len(mat[0])

        heights = [0] * cols
        INF = 10 ** 10
        ans = 0
        for r in range(rows):

            for c in range(cols):
                if mat[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0
            

            for right in range(cols):
                min_height = INF
                for left in range(right, -1, -1):
                    min_height = min(min_height, heights[left])
                    if min_height == 0:
                        break                
                    ans += min_height

        return ans

