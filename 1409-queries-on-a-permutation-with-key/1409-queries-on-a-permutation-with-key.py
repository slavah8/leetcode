class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = list(range(1, m + 1))
        print(perm)
        result = []
        for q in queries:
            index = perm.index(q)
            print(index)
            result.append(index)
            perm.pop(index)
            perm.insert(0, q)
        
        return result
        

        
