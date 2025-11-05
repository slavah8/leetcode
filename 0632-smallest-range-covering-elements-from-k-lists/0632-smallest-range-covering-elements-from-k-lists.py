class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        INF = 10 ** 10
        heap = []  # (value, list_id, index_in_list)
        curr_max = -INF

        for i in range(k): # first element of each list
            v = nums[i][0]
            heap.append((v, i, 0))
            curr_max = max(v, curr_max)

        heapq.heapify(heap)
        best_lo, best_hi = -INF, INF
        
        while len(heap) == k:
            lo, i, j = heap[0][0], heap[0][1], heap[0][2]
            if curr_max - lo < best_hi - best_lo or (curr_max - lo == best_hi - best_lo and lo < best_lo):
                best_lo, best_hi = lo, curr_max
            
            # try to increase best low by advancing that list's index by 1
            _, i, j = heapq.heappop(heap)
            if j + 1 == len(nums[i]):
                break
            nxt = nums[i][j + 1]
            curr_max = max(curr_max, nxt)
            heapq.heappush(heap, (nxt, i, j + 1))
        
        return [best_lo, best_hi]


        

