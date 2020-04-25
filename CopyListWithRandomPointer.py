__author__ = 'Jie'
"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.hs={} # key: old node, value: new node

    def copyRandomList_1(self, head: 'Node') -> 'Node':
        # the recursive method
        if head is None: return None  # the terminate condition
        if head in self.hs:
            new_node=self.hs[head]
        else:
            # create a new node and put it into hash table
            new_node=Node(head.val,None,None)
            self.hs[head]=new_node
            new_node.next=self.copyRandomList_1(head.next)
            new_node.random=self.copyRandomList_1(head.random)
        return new_node

    def copyRandomList_2(self,head):
        # iterative method

        def copyNode(node):
            # copy a Node to the following Node
            #
            if node is None: return None

            if node in self.hs:
                return self.hs[node]
            else:
                new_node=Node(node.val,None,None)
                self.hs[node]=new_node
                return self.hs[node]
        curr=head
        new_head=copyNode(head)  # loop pointer
        new_curr=new_head   # for the final output

        while curr:
            new_head.next=copyNode(curr.next)
            new_head.random=copyNode(curr.random)

            new_head=new_head.next
            curr=curr.next
        return new_curr




# [[7,null],[13,0],[11,4],[10,2],[1,0]]
# node=Node(7,node1,None)
# node.next=Node(13,)
solution=Solution()
# ans=solution.copyRandomList_1(head)