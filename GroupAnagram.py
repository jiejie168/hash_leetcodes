__author__ = 'Jie'
"""
49. Group Anagrams

Given an array of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        results=defaultdict(list) # create a default dictionary, with the form of {" ":[],"":[]}
        for s in strs:
            results[tuple(sorted(s))].append(s)  # if key is the same, add each value into [].
        # print (results)
        return results.values()

    def groupAnagrams_2(self,strs):
        # method 2, use count.
        # ord() gives the unicode code point of a character
        results=defaultdict(list)
        for s in strs:
            count=[0]*26 #
            for c in s:
                count[ord(c)-ord("a")]+=1  # the number of occurrence of each character
            results[tuple(count)].append(s)
        return results.values()

solution=Solution()
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
ans=solution.groupAnagrams_2(strs)
print (ans)

# aa=['a','b','a']
# dic=defaultdict(int)
# for elem in aa:
#     dic[elem]+=1
# print (dic)