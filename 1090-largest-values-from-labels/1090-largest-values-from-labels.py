class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        

        zipped = list(zip(values, labels))
        

        zipped.sort(key = lambda x: -x[0])
        print(zipped)
        
        total = 0
        i = 0
        n = len(values)
        used = defaultdict(int)
        while i < n and numWanted > 0:
            x = zipped[i][0]
            label = zipped[i][1]

            if used[label] < useLimit:
                total += x
                used[label] += 1
                numWanted -= 1
                i += 1
            else:
                i += 1
        
        return total



