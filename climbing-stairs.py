class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        
        odd, even, cur = 1, 2, 0
        for i in range(2, n):
            cur = odd + even
            odd, even = even, cur
        return cur
