__author__ = 'Jie'
"""
202. Happy Number

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
 replace the number by the sum of the squares of its digits,
 and repeat the process until the number equals 1 (where it will stay),
 or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        # the loop terminate condition is when n=1
        # use a hash table for check
        # noted:  A number will not be a Happy Number when it makes a loop in its sum sequence
        # that it saw the sums in this sequence which already been existed.

        hs_seen=set()
        while n!=1:
            sums=0 # the square sum
            curr=n  # the curr for loop
            while curr!=0:
                # find the sums square of each digit
                sums+=(curr%10)*(curr%10)
                curr=curr//10

            # check if the sums is already seen in hash table
            # return False if it has been seen.
            print (sums)
            if sums in hs_seen:
                return False
            hs_seen.add(sums)
            n=sums

        return True
solution=Solution()
ans=solution.isHappy(298982)
print (ans)


