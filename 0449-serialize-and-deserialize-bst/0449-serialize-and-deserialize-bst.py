# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []
        
        def traverse(node):
            if not node:
                return
            
            result.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        print(result)
        return ','.join(result)


        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return
        preorder = list(map(int, data.split(',')))
        INF = 10 ** 10
        i = 0
        def build(low, high):
            nonlocal i
            if i == len(preorder):
                return 
            v = preorder[i]
            if v > high or v < low:
                return
            i += 1
            node = TreeNode(v)
            node.left = build(low, v)
            node.right = build(v, high)
            return node
        
        return build(-INF, INF)

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans