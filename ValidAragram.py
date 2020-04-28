__author__ = 'Jie'
"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use the hash table
        if s is None:
            return False
        m=len(s)
        n=len(t)
        lookup=collections.defaultdict(int)

        if m!=n:
            return False
        # count all the characteristics in s and store them into hash table
        for i in s:
            lookup[i]+=1
        # check if chara in t is inside lookup
        for i in t:
            if i not in lookup:
                return False
            else:
                lookup[i]-=1
        # check if lookup is all 0
        for i in lookup.values():
            if i!=0:
                return False
        return True

    def isAnagram_1(self,s,t):
        return sorted(s)==sorted(t)

s = "anagram"
t = "nagaram"
solution=Solution()
# ans=solution.isAnagram(s,t)
ans=solution.isAnagram_1(s,t)
print (ans)




