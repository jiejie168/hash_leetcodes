__author__ = 'Jie'
"""
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words,
that are all of the same length. Find all starting indices of substring(s) in s
that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""
class Solution:
    def findSubstring(self, s: str, words):

        if s is None or len(words)==0:
            return []
        m=len(words)
        n=len(words[0])
        result=[]
        # creat a dictionary, with value starts with 0
        # estimate the number of each element in words
        hash_t=dict.fromkeys(words,0)
        for elem in words:
            hash_t[elem]+=1
        for i in range(len(s)-n*m+1):
            hash_copy=hash_t.copy()
            k=m
            j=i # i in big loop should be constant in the smaller loop
            while k>0:
                tmp=s[j:j+n]
                if tmp not in hash_copy or hash_copy[tmp]<1:
                    # under this condition, no substring, so break to the next big loop.
                    break
                else:
                    hash_copy[tmp]=hash_copy[tmp]-1
                k-=1
                j+=n
            if k==0:
                result.append(i)
        return result

# s = "wordgoodgoodgoodbestword",
# words = ["word","good","best","word"]
# s = "barfoothefoobarman"
# words = ["foo","bar"]
s="wordgoodgoodgoodbestword"
words=["word","good","best","good"]
solution=Solution()
ans=solution.findSubstring(s,words)
print (ans)

# L=["word","abc","word"]
# Dict = dict.fromkeys(L,0)
# for ele in L:
#     Dict[ele]=Dict[ele]+1
# print (Dict)
# from collections import defaultdict
# hash_t=defaultdict(int)
# for elem in L:
#     hash_t[elem]+=1
# print (hash_t)
# d2=Dict
# d2["cdefg"]=3
# print (d2)

