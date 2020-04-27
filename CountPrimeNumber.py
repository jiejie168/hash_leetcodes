__author__ = 'Jie'
import math
"""
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.
Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2: return 0
        # set all numbers to prime number
        res=[1]*n # prime number:res[n]=1; otherwise, res[n]=0
        res[0]=res[1]=0

        for i in range(2,math.floor(math.sqrt(n))+1):
            # print(not res[i])
            # start from 2, if res[i] is not prime, jump to the next i.
            if res[i]!=1:
                continue
            # is res[i] is prime, remove all the other numbers in i^2+i
            for j in range(i*i,n,i):
                res[j]=0
        count=sum(res)
        return count
n=10
solution=Solution()
ans=solution.countPrimes(n)
print (ans)