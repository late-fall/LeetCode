# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return '.'
        return ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        

    def deserialize(self, data):
        if not data:
            return
        
        return self.deserialize_helper(data.split(" "))
    
    def deserialize_helper(self, nodes):
        val = nodes.pop(0)
        if val == '.':
            return
        
        node = TreeNode(val)
        node.left = self.deserialize_helper(nodes)
        node.right = self.deserialize_helper(nodes)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))