# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node, subNode):
            if node is None and subNode is None:
                return True
            if node is None or subNode is None:
                return False

            if node.val == subNode.val:
                left = sameTree(node.left, subNode.left)
                right = sameTree(node.right, subNode.right)
                return left and right

            return False # if one of the trees is empty but the other isn't

        def isSubtree(node, subNode):
            if subNode is None:
                return True
            if node is None:
                return False
            if sameTree(node, subNode):
                return True
            left = isSubtree(node.left, subNode)
            right = isSubtree(node.right, subNode)
            return left or right

        return isSubtree(root, subRoot)