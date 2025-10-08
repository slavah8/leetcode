class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        counts1 = collections.Counter(arr1)
        counts2 = collections.Counter(arr2)
        counts3 = collections.Counter(arr3)
        keys_union = counts1.keys() | counts2.keys() | counts3.keys()
        result = []
        for x in keys_union:
            if x in counts1 and x in counts2 and x in counts3:
                result.append(x)
        return sorted(result)