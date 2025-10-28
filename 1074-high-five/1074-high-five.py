class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        id_scores = defaultdict(list)
        id_count = defaultdict(int)
        for ID, score in items:
            id_scores[ID].append(-score)
            id_count[ID] += 1
        
        result = []
        for ID in id_scores.keys():
            scores = id_scores[ID]
            heapify(scores)
            count = 0
            total = 0
            while scores and count < 5:
                score = heapq.heappop(scores)
                total += (-score)
                count += 1
            result.append((ID, total // count))
        return sorted(result, key = lambda x: x[0])

            

