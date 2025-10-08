class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort(key = lambda x: x[0])
        N = len(items)
        prefix = [0] * (N) # prefix max array for beauty 
        prefix[0] = items[0][1] 
        for i in range(1, N):
            prefix[i] = max(prefix[i - 1], items[i][1])
        print(items)
        print(prefix)
        res = []
        prices = [p for p, _ in items]
        print(prices)
        for x in queries:
            # need the max beauty of item with price <= query price
            index = bisect.bisect_right(prices, x) - 1
            res.append(prefix[index] if index >= 0 else 0)
        return res
