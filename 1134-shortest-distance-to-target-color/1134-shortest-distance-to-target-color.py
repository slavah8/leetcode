class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        result = []
        positions = defaultdict(list) # {color : indexes in array}
        for idx, color in enumerate(colors):
            positions[color].append(idx)
        INF = 10 ** 20
        for index, color in queries:
            if color not in positions:
                result.append(-1)
                continue
            idxs = positions[color]
            j = bisect.bisect_left(idxs, index)
            left = idxs[j - 1] if j > 0 else INF
            right = idxs[j] if j < len(idxs) else INF
            minn = min(abs(index - left), abs(index - right))
            result.append(minn)
            
        return result
            
