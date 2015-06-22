#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):

        slow = fast = n
        slow = self.digitSquareSum(slow)
        fast = self.digitSquareSum(fast)
        fast = self.digitSquareSum(fast)

        while slow != fast:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)

        return slow == 1

    def digitSquareSum(self, n):

        t = 0 
        while n != 0:
            t += (n%10) **2
            n /= 10
        return t

if __name__ == '__main__':
    s = Solution()
    print s.isHappy(2)
