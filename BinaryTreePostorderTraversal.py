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
        # use the iterative method
        # adopt the reverse_postorderTraversal:  pseudo code of recursive.
        # rev_postorder(root):
        #     if root is None:
        #         return
        #     print (node.val)
        #     rev_postorder(root-> right)
        #     rev_postorder(root-> left)

        if root is None:
            return
        stack1=[] # initialize stacks
        stack2=[] # stack for store the reversed results
        stack1.append(root)
        while stack1:
            # iterative for the reverse-postorder
            curr=stack1.pop()
            stack2.append(curr.val)
            if curr.left !=None:
                # be careful! the stack is LIFO, so last search right node in reverse,
                # equal to fist push left node in stack
                stack1.append(curr.left)
            if curr.right!=None:
                stack1.append(curr.right)
        while stack2:
            # reversed the output of stack2
            node=stack2.pop()
            stack1.append(node)
        return stack1
solution=Solution()
root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)
ans=solution.postorderTraversal_2(root)
print (ans)
