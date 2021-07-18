class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inner(root: TreeNode, count: int):
    if(root.left == None and root.right == None):
        return count
    else:
        if(root.left == None):
            return inner(root.right, count+1)
        elif(root.right == None):
            return inner(root.left, count+1)
        else:
            return min(inner(root.left, count+1), inner(root.right, count+1))

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        return inner(root, 0)+1
        


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

print(Solution.minDepth(TreeNode, root))