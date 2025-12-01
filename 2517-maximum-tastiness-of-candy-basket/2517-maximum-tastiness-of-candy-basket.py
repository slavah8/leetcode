class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        n = len(price)

        price.sort()
        print(price)
        # check if this maximum tastiness is feasible
        def check(tasty):
            
            selected = 1
            curr = price[0]
            for i in range(1, n):
                if curr + tasty <= price[i]:
                    selected += 1
                    curr = price[i]
            return selected >= k


        low = 0
        high = max(price)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
