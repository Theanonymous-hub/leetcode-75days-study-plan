class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return None
        q = deque()
        q.append(root)
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if(node.left):q.append(node.left)
                if(node.right):q.append(node.right)
            ans.append(temp)
        
        return ans
