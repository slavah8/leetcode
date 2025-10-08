class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        
        pos = {x : i for i, x in enumerate(target)}
        idx_seq = []
        for x in arr:
            if x in pos:
                idx_seq.append(pos[x])
        

        tails = []

        for v in idx_seq:
            i = bisect.bisect_left(tails, v)

            if i == len(tails):
                tails.append(v)
            else:
                tails[i] = v
        return len(target) - len(tails)