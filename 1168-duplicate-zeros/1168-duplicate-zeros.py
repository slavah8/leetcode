class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        zeroes = arr.count(0)
        N = len(arr)
        for i in range(N - 1, -1, -1):
            j = i + zeroes
            if j < N:
                arr[j] = arr[i]
            
            if arr[i] == 0:
                zeroes -= 1
                j = i + zeroes
                if j < N:
                    arr[j] = 0
