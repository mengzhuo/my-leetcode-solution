"""
https://leetcode.com/problems/count-primes/
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <=2:
            return 0
        if n == 3:
            return 1

        count = n-2
        
        d = [True for i in xrange(n)]
        
        for i in xrange(2, int(n**0.5)+1):
            if d[i]:
                j = 2
                while i*j < n:
                    if d[i*j]:
                        d[i*j] = False
                        count -=1
                    j +=1


        return count
