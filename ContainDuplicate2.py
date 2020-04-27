__author__ = 'Jie'
"""
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct
indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        # utilize hash table to restore numbers: hs[elem]=index
        # noted that: in case multiple duplicates occur, replace the first index of the duplicate elem with following index
        hs={}
        for i, elem in enumerate(nums):
            if elem not in hs:
                # add elem when it is not inside the hash table
                hs[elem]=i
            else:
                if i-hs[elem]<=k:
                    return True
                # in case the occurrence of many duplicates (>2)
                hs[elem]=i
        return False

solution=Solution()
nums = [1,0,1,1]
k = 1
ans=solution.containsNearbyDuplicate(nums,k)
print (ans)