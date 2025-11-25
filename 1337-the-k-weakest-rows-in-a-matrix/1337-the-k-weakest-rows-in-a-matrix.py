class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])

        counts = [0] * rows

        for r in range(rows):
            count = 0
            for c in range(cols):
                if mat[r][c] == 1:
                    count += 1
            counts[r] = count
        
        print(counts)

        sorted_counts = []
        for r, cnt in enumerate(counts):
            sorted_counts.append((cnt, r))
        
        sorted_counts.sort(key = lambda x: (x[0], x[1]))
        print(sorted_counts)

        ans = []
        k = k
        for cnt, row in sorted_counts:
            ans.append(row)
            k -= 1
            if k == 0:
                break
        return ans