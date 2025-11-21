class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        n = nodes - 1
        subtree_vals = [0] * nodes
        subtree_sizes = [0] * nodes
        parent_to_nodes = defaultdict(list)
        removed = [False] * nodes
        for node, p in enumerate(parent):
            parent_to_nodes[p].append(node)

        ans = nodes
        def dfs(i, p):
            size = 1
            subtree_sum = value[i]

            if i not in parent_to_nodes:
                if subtree_sum == 0:
                    removed[i] = True
                subtree_sizes[i] = size
                return subtree_sum, size
            
            
            for nei in parent_to_nodes[i]:
                child_sum, child_size = dfs(nei, i)
                subtree_sum += child_sum
                size += child_size
            
            
            subtree_vals[i] = subtree_sum
            subtree_sizes[i] = size
            if subtree_sum == 0:
                removed[i] = True
            return subtree_sum, size
            
        
        dfs(0, -1)
        
        def remove(node):
            for nei in parent_to_nodes[node]:
                removed[nei] = True
                remove(nei)

        for node in range(nodes):
            if removed[node]:
                for nei in parent_to_nodes[node]:
                    removed[nei] = True
                    remove(nei)
        
        print(removed)
        return removed.count(False)