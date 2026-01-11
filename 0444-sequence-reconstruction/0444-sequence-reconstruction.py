class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        indegree = [0] * (n + 1)
        seen = set()
        graph = [set() for _ in range(n + 1)]
        
        for seq in sequences:
            for x in seq:
                seen.add(x)
            
            for a, b in zip(seq, seq[1:]):
                if b not in graph[a]:
                    indegree[b] += 1
                    graph[a].add(b)

        
        if len(seen) != n:
            return False

        # kahns algorithm

        q = deque(node for node in range(1, n + 1) if indegree[node] == 0)

        
        for i in range(n):

            if len(q) != 1:
                return False

            cur = q.popleft()

            if cur != nums[i]:
                return False
            
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return True

        

                
                