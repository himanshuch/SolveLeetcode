# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001

        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            self.res = max(self.res, root.val+max(0,leftMax)+max(0,rightMax))
            root.val += max(leftMax, rightMax, 0)
            return root.val

        dfs(root)
        return self.res