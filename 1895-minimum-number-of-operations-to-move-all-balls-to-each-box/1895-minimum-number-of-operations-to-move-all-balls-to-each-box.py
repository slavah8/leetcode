class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        answer = [0] * N
        for i in range(N):
            for j in range(N):
                if i != j and boxes[j] == '1':
                    answer[i] += abs(i - j)
        return answer
