# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        queue = [root]

        #def bfs(root, curr):
        #    if not root:
        #        return
        #    queue.append(root)
        #    curr.append(root.val)

        while queue:
            #curr=[]
            rightSide = None
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
                #bfs(node.left, curr)
                #bfs(node.right, curr)
            #if len(curr):
            #    ans.append(curr[-1])
            if rightSide:
                ans.append(rightSide.val)
        
        return ans