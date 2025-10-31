class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)

        running_sum = [0] * (n + 1)

        for i in range(n):
            running_sum[i + 1] = running_sum[i] + (1 if possible[i] == 1 else -1)
        
        print(running_sum)

        # find min index i where prefix[i] > prefix(n) - prefix[i + 1]

        for i in range(1, n):
            if running_sum[i] > running_sum[n] - running_sum[i]:
                return i
        return -1