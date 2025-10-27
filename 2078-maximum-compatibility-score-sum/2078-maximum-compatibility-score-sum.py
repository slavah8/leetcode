class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        M, N = len(students), len(students[0])
        # score[i][j] = compatibility between student i and mentor j
        score = [[0] * M for _ in range(M)]

        for i in range(M):
            for j in range(M):
                same = 0
                for k in range(N):
                    if students[i][k] == mentors[j][k]:
                        same += 1
                score[i][j] = same
        
        print(score)

        # dp[mask] : maximum total compatibility for assigning mentors in mask to the first popcount(mask) students
        def dp(mask):
            i = mask.bit_count() # next student index
            if i == len(students):
                return 0
            best = 0
            for j in range(M):
                if (mask >> j) & 1 == 1: # continue if mentor j already used
                    continue
                best = max(best, score[i][j] + dp(mask | (1 << j)))
            return best
        return dp(0)