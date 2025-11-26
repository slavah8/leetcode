class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        n = len(citations)
        low = 0
        high = n - 1
        print(citations)
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1
        
        return n - low if low < n else 0