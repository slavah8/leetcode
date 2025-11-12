class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        
        child_map = defaultdict(list) # parent : children
        n = len(edges)
        for u, v in edges:
            child_map[u].append(v)
            child_map[v].append(u)
        

        subtree_sizes = [0] * (n + 1)
        good = 0
        def dfs(node, parent):
            nonlocal subtree_sizes
            nonlocal good
            size = 1
            child_sizes = []
            
            for child in child_map[node]:
                if child == parent:
                    continue
                child_size = dfs(child, node)
                size += child_size
                child_sizes.append(child_size)
            if len(child_sizes) == 0:
                good += 1
            if len(set(child_sizes)) == 1:
                good += 1
            
            subtree_sizes[node] = size
            return size

        dfs(0, -1)
        
        
        return good
