"""
2 的倍数就意味着只有一位是1
所以减一之后，与操作就知道是不是只有一位1了
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n & (n-1)) ==0


