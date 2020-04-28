__author__ = 'Jie'
"""
76. Minimum Window Substring
Hard

Given a string S and a string T, find the minimum window in S which
 will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use the sliding windows method
        if s is None:
            return ""
        if len(s)<len(t):
            return ""

        left,right=0,0 # two search pointers.
        wins={}  # key: character ; value: frequency
        map_t=collections.Counter(t) # count the frequency of unique character in t.
        count=0  # the flag to check if unique character appear, the maximum count is equal to len(map_t)
        required=len(map_t)
        res=(float("inf"),None,None)  # (minimun length, left index, right index)

        while right<len(s):
            # fix left index, start search via extend right index
            tmp=s[right]
            wins[tmp]=wins.get(tmp,0)+1
            if tmp in map_t and wins[tmp]==map_t[tmp]:
                count+=1

            # fix right index, start search via contract left index
            # the second condition count==required is required
            while left<=right and count==required:
                tmp=s[left]
                # first restore the first valid substring (index width)
                if right-left<res[0]:
                    res=(right-left,left,right)
                wins[tmp]-=1 # the current tmp is not belong to wins any more
                # contract the left index.
                if tmp in map_t and wins[tmp]<map_t[tmp]:
                    count-=1
                left+=1
            right+=1
        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]

solution=Solution()
s="ADOBECODEBANC"
t="ABC"
ans=solution.minWindow(s,t)
print (ans)

