class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        

        seen = defaultdict(list) # value : idxs
        
        n = len(arr)
        
        for i, x in enumerate(arr):
            seen[x].append(i)
        
        print(seen)
        ans = [0] * n

        for val, idxs in seen.items():
            m = len(idxs)
            if m == 1:
                continue

            prefix = [0] * (m)
            prefix[0] = idxs[0]
            for t in range(1, m):
                prefix[t] = prefix[t - 1] + idxs[t]
            print(prefix)
            total_sum = prefix[-1]
            for k, x in enumerate(idxs):
                # left side: indices 0..k-1
                left = x * k - prefix[k - 1] if k > 0 else 0
                # right side: indices k+1..m-1
                right_sum = total_sum - prefix[k]
                right_cnt = m - k - 1
                right = right_sum - right_cnt * x
            
                ans[x] = left + right

        return ans