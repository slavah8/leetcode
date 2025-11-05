class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = [(-s, i) for i, s in enumerate(score)]

        heapify(heap)
        
        answer = [0] * n
        i = 0
        while heap:
            s, idx = heapq.heappop(heap)
            if i == 0:
                answer[idx] = 'Gold Medal'
            elif i == 1:
                answer[idx] = 'Silver Medal'
            elif i == 2:
                answer[idx] = 'Bronze Medal'
            else:
                answer[idx] = str(i + 1)
            i += 1
        return answer
            
