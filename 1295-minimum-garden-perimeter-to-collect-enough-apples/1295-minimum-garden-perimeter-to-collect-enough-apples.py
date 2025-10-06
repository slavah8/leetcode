class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        
        def apples(n):
            return 2 * (2 * n + 1) * n * (n + 1)
        
        # calculating how big of a radius n we need to fit neededApples

        low = 0
        high = 1
        while apples(high) < neededApples:
            high *= 2
        
        while low < high:
            mid = (low + high) // 2
            if apples(mid) >= neededApples:
                high = mid
            else:
                low = mid + 1
        n = low
        return 8 * n