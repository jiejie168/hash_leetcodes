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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        # use the iterative algorithm, Morris Traversal
        res=[]
        curr=root
        while curr !=None:
            if curr.left==None:
                # directly output the val of current tree node
                # and then turn to the right node of current
                res.append(curr.val)
                curr=curr.right
            else:
                # the current has left subtree
                pre=curr.left
                while pre.right!=None and pre.right!=curr:
                    # find the rightmost node
                    pre=pre.right
                pre.right=curr   # the curr node becomes the right node of pre.
                tmp=curr  # store the current node
                curr=curr.left # update the current point, which is the left node of current.
                tmp.left=None  #set the original current left to null, avoid infinite loop
        return res

    def inorderTraversal_3(self,root):
        # use iterative and stack.
        curr=root
        stacks=[] # initialize a stack
        res=[]
        while True:
            # keep search
            if curr !=None:
                # put the current to the stack, and  search the left until None
                stacks.append(curr)
                curr=curr.left
            elif stacks:
                # pop the element in stack, and print.
                curr=stacks.pop()
                res.append(curr.val)
                curr=curr.right # second search the right
            else:
                break
        return res

solution=Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

ans=solution.inorderTraversal_3(root)
print (ans)