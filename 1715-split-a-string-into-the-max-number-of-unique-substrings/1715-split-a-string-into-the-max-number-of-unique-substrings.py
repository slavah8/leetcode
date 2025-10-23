class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        longest = 0
        N = len(s)
        partition = []
        result = []
        seen = set()
        def dfs(index):
            nonlocal longest
            if index == N:
                if len(partition[:]) > longest:
                    longest = len(partition[:])
                return

            for j in range(index, N):
                if s[index:j + 1] in seen:
                    continue
                # choose this partition
                partition.append(s[index:j + 1])
                seen.add(s[index:j + 1])
                dfs(j + 1)
                partition.pop()
                seen.remove(s[index:j + 1])

                # skip this partition
        dfs(0)
        return longest





