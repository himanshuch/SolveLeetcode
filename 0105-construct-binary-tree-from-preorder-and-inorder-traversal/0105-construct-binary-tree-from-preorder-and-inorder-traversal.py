# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def constructTree(bt, inorder):

            if not len(preorder) or not len(inorder):
                return
                
            # assign the root as 1st value of preorder is the root.
            root = preorder.pop(0)
            bt = TreeNode(root)
            mid = inorder.index(root)

            bt.left = constructTree(bt.left, inorder[0:mid])
            bt.right = constructTree(bt.right, inorder[mid+1:])
            return bt

        return constructTree(None, inorder)
