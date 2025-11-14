class Solution:
    def maximizeGreatness(self, arr: List[int]) -> int:
        arr.sort()
        print(arr)
        i = 0
        j = 1
        n = len(arr)
        count = 0

        while i < n and j < n:
            while j < n and arr[i] >= arr[j]:
                j += 1
            print(i)
            print(j)
            if j < n and arr[j] > arr[i]:
                count += 1
            i += 1
            j += 1
        return count


