__author__ = 'Jie'
"""
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def postorderTraversal(self, root: TreeNode):
        # naive algorithm, using recursive
        res=[]
        self.helper(root,res)
        return res

    def helper(self,root,res):
        if root is None:
            # the terminate condition
            return
        if root.left !=None:
            self.helper(root.left,res)
        if root.right !=None:
            self.helper(root.right,res)
        res.append(root.val)

    def postorderTraversal_2(self,root):
        pass

solution=Solution()
root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)
ans=solution.postorderTraversal(root)
print (ans)
