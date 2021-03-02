# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSums(self, root: TreeNode) -> List[int]:
        # edge case, empty tree
        if root == None:
            return []
        # base case, single node (a leaf without children)
        if root.left == None and root.right == None:
            return [root.val]
        else:
            left_sums = self.findSums(root.left)
            right_sums = self.findSums(root.right)
            if left_sums == []:
                new_sum = right_sums[-1] + root.val
            elif right_sums == []:
                new_sum = left_sums[-1] + root.val
            else:
                new_sum = left_sums[-1] + right_sums[-1] + root.val
            sum_list = left_sums + right_sums + [new_sum]
            return sum_list
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
            sum_list = self.findSums(root)
            frequency = {}
            for i in sum_list:
                if i not in frequency:
                    frequency[i] = 1
                else:
                    frequency[i] += 1
            most_frequent = [key for key, value in frequency.items() if value == max(frequency.values())]
            return most_frequent
