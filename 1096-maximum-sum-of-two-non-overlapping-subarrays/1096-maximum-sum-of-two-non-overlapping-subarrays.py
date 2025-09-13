class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        A = firstLen
        B = secondLen
        N = len(nums)

        P = [0] * (N + 1)

        for i in range(N):
            P[i + 1] = P[i] + nums[i]
        
        sumA = [0] * (N - A + 1)
        for i in range(N - A + 1):
            sumA[i] = P[i + A] - P[i]
        
        sumB = [0] * (N - B + 1)
        for i in range(N - B + 1):
            sumB[i] = P[i + B] - P[i]
        print(P)
        print(sumB)

        best = 0
        for i in range(N - A + 1):
            a_sum = sumA[i]
            a_left = i
            a_right = i + A - 1
            for j in range(N - B + 1):
                b_sum = sumB[j]
                b_left = j
                b_right = j + B - 1
                # non overlap if A ends before B or A starts after B
                if a_right < b_left or a_left > b_right:
                    cand = a_sum + b_sum
                    if cand > best:
                        best = cand
        return best