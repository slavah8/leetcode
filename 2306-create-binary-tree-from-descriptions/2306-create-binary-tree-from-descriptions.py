# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = set()
        p_to_c = defaultdict(list)
        children = set()
        for parent, child, is_left in descriptions:
            children.add(child)
            p_to_c[parent].append((child, is_left))
            nodes.add(parent)
            nodes.add(child)

        print(p_to_c)
        print(children)
        print(nodes)
        for x in nodes:
            if x not in children:
                root = TreeNode(x)
                break

        def build(node):
            if not node:
                return
            for child, is_left in p_to_c[node.val]:
                if is_left == 1:
                    node.left = build(TreeNode(child))
                    
                else:
                    node.right = build(TreeNode(child))
                    
            return node
        
        return build(root)
