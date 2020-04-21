__author__ = 'Jie'
"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash_table
        n=len(s)
        maxL=0   # set the maximum length of substring
        start=-1  # according to the description, max=1 when s is None. so start is set to -1
        dict={}  # hash table. key is alphabet, value is the index of alphabet
        for i in range(n):
            if s[i] in dict and dict[s[i]]>start:
                # update the new start index, and replace the value of s[i] by current i index
                start=dict[s[i]]
                dict[s[i]]=i
            else:
                # if not in, add the index to hash table
                dict[s[i]]=i
                if i-start>maxL:
                    maxL=i-start
        return maxL


solution=Solution()
s=" "
ans=solution.lengthOfLongestSubstring(s)
print (ans)


