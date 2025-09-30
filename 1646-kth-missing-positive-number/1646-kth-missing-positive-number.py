class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for x in range(2001):
            if x not in arr:
                count += 1
                if count == k + 1:
                    return x