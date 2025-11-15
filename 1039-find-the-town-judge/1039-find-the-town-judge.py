class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for a, b in trust:
            graph[a].append(b)
            indegree[b] += 1
            outdegree[a] += 1
        
        print(indegree)
        print(outdegree)
        for i, (inn, out) in enumerate(zip(indegree, outdegree)):
            if indegree[i] == len(indegree) - 2 and  outdegree[i] == 0:
                return i
        
        return -1
