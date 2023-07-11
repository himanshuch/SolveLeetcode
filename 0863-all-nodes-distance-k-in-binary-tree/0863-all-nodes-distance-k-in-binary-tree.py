# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res =[]
        child_parent = {root: None}

        # maintain child-parent relationship
        def dfs(root):
            if not root:
                return
            if root.left:
                child_parent[root.left] = root
                dfs(root.left)
            if root.right:
                child_parent[root.right] = root
                dfs(root.right)
        
        dfs(root)

        q=deque()
        q.append(target)
        visited=[]

        while q and k:
            q_len = len(q)
            #if k ==0 : break
            while q_len:
                curr = q.popleft()
                visited.append(curr.val)
                q_len -=1
                node= child_parent[curr] #get parent node from child_parent map.
                if node and node.val not in visited: q.append(node) #append parent node to queue
                if curr.left and curr.left.val not in visited: q.append(curr.left) #append left node to queue
                if curr.right and curr.right.val not in visited: q.append(curr.right) #right
            k-=1

        while q:
            res.append(q.popleft().val)
        return res

