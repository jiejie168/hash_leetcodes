__author__ = 'Jie'
"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        # recursive method
        res=[]
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if root:
            if root.left:
                self.helper(root.left,res)
            res.append(root.val)
            if root.right:
                self.helper(root.right,res)
    def inorderTraversal_2(self,root):
        # use the iterative algorithm



# solution=Solution()
# root=[1,"null",2,3]
# ans=solution.inorderTraversal(root)
# print (ans)
