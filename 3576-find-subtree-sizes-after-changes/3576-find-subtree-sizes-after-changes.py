class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        child_map = defaultdict(list) # parent : children

        new_parent = parent[:]

        for node, p in enumerate(parent):
            child_map[p].append(node)
        

        last = [-1] * 26
        def dfs(node):
            idx = ord(s[node]) - ord('a')
            cand = last[idx]

            if node != 0 and cand != -1:
                new_parent[node] = cand
            else:
                new_parent[node] = parent[node]
            
            prev = last[idx]
            last[idx] = node
            for child in child_map[node]:
                dfs(child)

            # backtrack so that only real ancestors match
            last[idx] = prev

        dfs(0)
        new_children = defaultdict(list)

        for node, p in enumerate(new_parent):
            new_children[p].append(node)

        

        size = [0] * n
        # calculate subtree sizes
        def dfs(node):
            total = 1
            for child in new_children[node]:
                total += dfs(child)
            size[node] = total
            return total

        dfs(0)
        return size
