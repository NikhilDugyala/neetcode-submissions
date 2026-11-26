# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            level= []
            for i in range(len(queue)):
                print("queue", queue)
                node = queue.popleft()
                level.append(node.val)
                print(level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            out.append(level)

                
        return out

                





        