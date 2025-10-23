class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        

        N = len(seats)
        left = [-1] * N
        last = -1
        for i in range(N):
            if seats[i] == 1:
                last = i
            left[i] = last
        

        right = [N] * N
        last = N
        for i in range(N - 1, -1, -1):
            if seats[i] == 1:
                last = i
            right[i] = last
        
        best = 0
        INF = 10 ** 20
        for i in range(N):
            if seats[i] == 1:
                continue
            
            left_dist = INF if left[i] == -1 else i - left[i]
            right_dist = INF if right[i] == N else right[i] - i
            best = max(best, min(left_dist, right_dist))
        return best


