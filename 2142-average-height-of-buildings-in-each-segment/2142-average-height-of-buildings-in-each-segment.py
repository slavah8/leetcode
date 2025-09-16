class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        cntDelta = defaultdict(int)
        sumDelta = defaultdict(int)

        for L, R, height in buildings:
            cntDelta[L] += 1
            cntDelta[R] -= 1
            sumDelta[L] += height
            sumDelta[R] -= height
        
        running_sum = 0
        running_count = 0
        prev = None
        res = []
        for x in sorted(set(cntDelta.keys()) | set(sumDelta.keys())):
            if prev is not None and prev < x and running_count > 0:
                avg = running_sum // running_count
                if res and res[-1][2] == avg and res[-1][1] == prev:
                    res[-1][1] = x
                else:
                    res.append([prev, x, avg])

            running_sum += sumDelta[x]
            running_count += cntDelta[x]
            prev = x
        return res
