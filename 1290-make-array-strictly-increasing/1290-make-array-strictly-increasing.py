class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        arr2 = sorted(set(arr2))
        INF = 10 ** 20

        # best[ops] = smallest tail value achievable after processing up to current index
        best = {0 : -INF} 

        for a in arr1:
            nxt = {}

            # Option A: keep a if strictly increasing
            for ops, last in best.items():
                if a > last:
                    # But before we overwrite nxt[ops], we need to make sure:
                    # This path gives a smaller tail than what we already had for the same number of operations.
                    if ops not in nxt or a < nxt[ops]:
                        nxt[ops] = a

                # Option B: replace a with the smallest b in arr2 such that b > last
                j = bisect.bisect_right(arr2, last)
                if j < len(arr2):
                    b = arr2[j]
                    if (ops + 1) not in nxt or b < nxt[ops + 1]: # smaller tail with the same number of ops
                        nxt[ops + 1] = b
            if not nxt:
                return -1
            best = nxt

        return min(best)

