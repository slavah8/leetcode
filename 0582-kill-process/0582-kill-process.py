class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        ans = []

        child_map = defaultdict(list)
        for node, p in enumerate(ppid):
            if p == 0:
                continue
            child_map[p].append(pid[node])
        
        print(child_map)
        def dfs(node):
            nonlocal ans, child_map
            ans.append(node)
            for child in child_map[node]:
                dfs(child)
            
            
            

        

        dfs(kill)
        return ans