class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        segment = ""
        result = []
        for i, char in enumerate(s):
            candidate = segment + char
            if candidate not in seen:
                result.append(candidate)
                seen.add(candidate)
                segment = ""
            else:
                segment = candidate
            
            
            
        return result
