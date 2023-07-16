# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not len(inorder) or not len(postorder):
            return
        # In post-order end is always the root...
        root = postorder.pop()
        res = TreeNode(root)

        mid = inorder.index(root)
        res.right = self.buildTree(inorder[mid+1:], postorder)
        res.left = self.buildTree(inorder[0:mid], postorder)

        return res
