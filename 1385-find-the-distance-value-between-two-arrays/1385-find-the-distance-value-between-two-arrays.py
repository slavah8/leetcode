class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n = len(arr1)
        m = len(arr2)
        count = 0

        for i in range(n):
            x = arr1[i]
            ok = True
            for j in range(m):
                if abs(x - arr2[j]) <= d:
                    ok = False
                    break
            if ok:
                count += 1
        return count
                