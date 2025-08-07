class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True  # Both are None
            if not p or not q:
                return False  # One is None, the other isn't
            if p.val != q.val:
                return False  # Values differ

            # Recursively check left and right
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
