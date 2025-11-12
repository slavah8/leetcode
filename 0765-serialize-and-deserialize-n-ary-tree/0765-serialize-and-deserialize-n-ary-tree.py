"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return '[]'

        def preorder(node):
            s = str(node.val)
            if node.children:
                s += '[' + ' '.join(preorder(child) for child in node.children) + ']'
            return s
        return '[' + preorder(root) + ']'
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        
        
        s = data.strip()
        if s == '[]':
            return None
            
        if s[0] == '[' and s[-1] == ']':
            s = s[1:-1]
        n = len(s)
        i = 0

        # advance past any whitespace
        def skip(i):
            while i < n and s[i].isspace():
                i += 1
            return i
        
        def parse_int(i):
            i = skip(i)
            j = i
            while j < n and s[j].isdigit():
                j += 1
            return int(s[i:j]), j
        
        def parse_node(i):
            val, i = parse_int(i)
            node = Node(val, [])


            i = skip(i)
            if i < n and s[i] == '[':
                i += 1
                i = skip(i)
                while i < n and s[i] != ']':
                    child, i = parse_node(i)
                    node.children.append(child)
                    i = skip(i)
                if i < n and s[i] == ']':
                    i += 1
            return node, i
        
        root, _ = parse_node(0)
        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))