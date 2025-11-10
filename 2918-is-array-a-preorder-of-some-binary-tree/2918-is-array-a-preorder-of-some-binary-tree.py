class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        
        root_id, root_p = nodes[0]
        if root_p != -1:
            return False
        
        stack = [root_id] # the current path from the root to the node you just read (root at bottom, current node at top).
        seen = {root_id}


        for k in range(1, len(nodes)):
            node, parent = nodes[k]

            if node in seen:
                return False
            
            seen.add(node)

            while stack and stack[-1] != parent:
                stack.pop()
            
            if not stack or stack[-1] != parent:
                return False
            
            stack.append(node)
        return True
            

