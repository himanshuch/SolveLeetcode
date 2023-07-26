# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root is None:
                return None
            if root == p or root == q:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right: #if both left and right are not null return root which is the LCA
                return root
            else:
                return left or right # return whichever is not null
            
            '''
            OR
            elif left is None:
                return right
            else:
                return left
            '''
            
        return dfs(root)


        