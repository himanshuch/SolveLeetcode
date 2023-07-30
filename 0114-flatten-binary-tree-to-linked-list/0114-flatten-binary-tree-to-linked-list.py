# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root

        while cur: # while cur is not null
            if cur.left: #if cur.left exists
                pred = cur.left
                # find predecessor
                while pred.right:
                    pred = pred.right
                # link updated nodes
                pred.right = cur.right # predecessor right points to current right
                cur.right = cur.left # current right points to current left
                cur.left = None # set current left to None as mentioned.
            cur = cur.right # move current to current right which is actully current left before setting it to null....

