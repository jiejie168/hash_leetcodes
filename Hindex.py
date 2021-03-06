__author__ = 'Jie'
"""
274. H-Index
M
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each,
and the other N ? h papers have no more than h citations each."

Example:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""

class Solution:
    def hIndex(self, citations) -> int:
        # the basic idear is to find the index where citations[index]>=index
        if not citations:
            return 0
        n=len(citations)
        citations=sorted(citations,reverse=True)  # from large to small
        i=0
        while i<n and citations[i]>=i:
            i+=1
        return i



