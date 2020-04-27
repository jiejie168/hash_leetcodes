__author__ = 'Jie'
"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use hash method.
        if nums is None:
            return False
        # hs=collections.defaultdict(int)
        hs=set()  # define a set for restore the number in list
        for elem in nums:
            if elem in hs:
                return True
            hs.add(elem)
        return False
