# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.queue = deque()

        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val):
        new_node = TreeNode(val)
        parent = self.queue[0]

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.queue.popleft() 

        self.queue.append(new_node)
        return parent.val

    def get_root(self):
        return self.root
      


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()