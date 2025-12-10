class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        rows = len(score)
        cols = len(score[0])

        row_scores = []
        for r in range(rows):
            s = score[r][k]
            row_scores.append((s, r))
        
        row_scores.sort(key = lambda x: x[0], reverse = True)
        print(row_scores)

        new_score = [[] * cols for _ in range(rows)]
        
        for i, (_, row) in enumerate(row_scores):
            new_score[i] = score[row]
        
        return new_score

        
