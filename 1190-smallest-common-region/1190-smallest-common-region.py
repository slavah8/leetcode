class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        
        children = defaultdict(list) # parent : children
        nodes = set()
        all_children = set()
        for group in regions:
            p = group[0]
            nodes.add(p)
            for c in group[1:]:
                children[p].append(c)
                nodes.add(c)
                all_children.add(c)
        
        roots = list(nodes - all_children)
        root = roots[0]

        def dfs(node, target):
            if node == target:
                return [node]
            
            for nei in children[node]:
                sub = dfs(nei, target)
                if sub is not None:
                    return [node] + sub
            return None
            
        p1 = dfs(root, region1)
        p2 = dfs(root, region2)
        print(p1)
        print(p2)
        i = 0
        while i < len(p1) and i < len(p2) and p1[i] == p2[i]:
            i += 1
        return p1[i - 1]

            




        