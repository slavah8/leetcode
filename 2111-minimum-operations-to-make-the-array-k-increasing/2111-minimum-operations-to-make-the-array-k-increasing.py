class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        
        # Helper: length of Longest Non-Decreasing Subsequence of seq
        def LNDS_length(seq):
            tails = []
            for x in seq:
                pos = bisect.bisect_right(tails, x)
                if pos == len(tails):
                    tails.append(x)
                else:
                    tails[pos] = x
            return len(tails)
        n = len(arr)
        ops = 0
        for start in range(k):
            seq = []
            for i in range(start, n, k):
                seq.append(arr[i])
            
            keep = LNDS_length(seq)
            ops += len(seq) - keep
        return ops
