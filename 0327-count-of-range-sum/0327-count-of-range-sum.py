class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        N = len(nums)
        P = [0] * (N + 1)

        for i in range(N):
            P[i + 1] += P[i] + nums[i]

        
        def solve(low, high):
            if high - low <= 1:
                return 0
            
            mid = (low + high) // 2
            count = solve(low, mid) + solve(mid, high)

            left_vals = P[low:mid]
            L = R = mid
            for x in left_vals:
                while L < high and P[L] < x + lower:
                    L += 1
                while R < high and P[R] <= x + upper:
                    R += 1
                count += (R - L)
            
            merged = []
            i, j = low, mid
            while i < mid and j < high:
                if P[i] <= P[j]:
                    merged.append(P[i])
                    i += 1
                else:
                    merged.append(P[j])
                    j += 1
            merged.extend(P[i:mid])
            merged.extend(P[j:high])
            P[low:high] = merged

            return count
        
        return solve(0, N + 1)
