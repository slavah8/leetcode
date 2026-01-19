class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        total = 0
        for i in range(n):
            for j in range(i + 1):
                sub = arr[j:i + 1]
                print(sub)
                if len(sub) % 2 == 1:
                    total += sum(sub)
        
        return total

        