class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        rows = len(mat)
        cols = len(mat[0])

        
        curr_sums = mat[0][:]
        if len(curr_sums) > k:
            curr_sums = curr_sums[:k]
        
        for r in range(1, rows):
            row = mat[r]

            next_sums = []
            heap = []

            for i in range(min(k, len(curr_sums))):
                heapq.heappush(heap, (row[0] + curr_sums[i], i, 0))
            
            for _ in range(min(k, len(curr_sums) * len(row))):
                s, i, j = heapq.heappop(heap)
                next_sums.append(s)
                if j + 1 < len(row):
                    new_sum = curr_sums[i] + row[j + 1]
                    heapq.heappush(heap, (new_sum, i, j + 1))
                
                if len(next_sums) == k:
                    break
            
            curr_sums = next_sums
        return curr_sums[k - 1]