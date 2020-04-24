__author__ = 'Jie'

"""
144. Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root) :
        # use the recursive algorithm
        res=[]
        self.helper(root,res)
        return res

    def helper(self,root,res):
        if root:
            # if current node exist, output the node directly
            res.append(root.val)
            if root.left:
                self.helper(root.left,res)
            if root.right:
                self.helper(root.right,res)

    def preorderTraversal_1(self,root):
        # method 2, use the iterative algorithm
        # creat a stack for storing the nodes
        if root is None:
            return
        res=[]
        stacks=[]
        stacks.append(root)
        while len(stacks)>0:
            # as long as stacks is not 0, pop up and output the element value
            curr=stacks.pop()
            res.append(curr.val)
            if curr.right is not None:
                # the added sequence has been changed for stack during iterative
                stacks.append(curr.right)
            if curr.left is not None :
                stacks.append(curr.left)
        return res

solution=Solution()
root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)

ans=solution.preorderTraversal_1(root)
print (ans)