# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        og_root = root
        
        # Empty tree?
        if root is None:
            return 0
        # Only root?
        if root.left is None and root.right is None:
            return 1
        # Base case
        if root.right is None:
            print("base case!")
            return 2
        
        # Traverse as far possible left, counting how many rows
        row_count = 0
        while root.left:
            row_count += 1
            parent = root
            root = root.left
       
        # Traverse as far right as possible, counting rows
        root = og_root
        right_row_count = 0
        while root.right:
            right_row_count += 1
            right_parent = root
            root = root.right
            
        # if row_count and right_row_count is equal, then tree is completely full
        if row_count == right_row_count:
            count = 0
            for i in range(row_count+1):
                count += 2**i
            print("full!", count)
            return count
        
        # else, recurse on the two subtrees and add as you go
        return 1 + self.countNodes(og_root.right) + self.countNodes(og_root.left)
        
