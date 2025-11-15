class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = defaultdict(list)
        for node, p in enumerate(parent):
            graph[p].append(node)
        
        ans = 1
        def dfs(node):
            nonlocal ans
            longest1 = 0
            longest2 = 0
            for nei in graph[node]:
                child_len = dfs(nei)

                if s[nei] != s[node]: # can extend with this child
                    if child_len > longest1:
                        longest2 = longest1
                        longest1 = child_len
                        
                    elif child_len > longest2:
                        longest2 = child_len

            ans = max(ans, longest1 + longest2 + 1)
                    
                
            return 1 + longest1
            
            
        dfs(0)
        return ans


