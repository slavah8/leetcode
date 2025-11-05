class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        answer = [0] * n
        
        idx = list(range(n))
        idx.sort(key = lambda i: nums1[i])
        print(idx)

        heap = []
        heap_sum = 0
        i = 0

        while i < n:
            v = nums1[idx[i]]
            j = i
            while j < n and nums1[idx[j]] == v:
                j += 1
            
            for t in range(i, j):
                answer[idx[t]] = heap_sum
            
            for t in range(i, j):
                z = nums2[idx[t]]
                if len(heap) < k:
                    heapq.heappush(heap, z)
                    heap_sum += z
                elif z > heap[0]:
                    x = heapq.heappop(heap)
                    heap_sum -= x
                    heapq.heappush(heap, z)
                    heap_sum += z
            i = j
        return answer




            
            

